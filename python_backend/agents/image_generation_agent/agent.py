from google.adk import Agent
from tools.generate_image import image_creator
from tools.image_checker import image_checker
from google import genai
from google.genai import types
import re
import base64  # add this import at the top of your file
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()


# Set up genai client once
client = genai.Client()


class ImageGenerationAgent(Agent):
    async def _run_async_impl(self, ctx):
        print("🎨 Inside ImageGenerationAgent")
        last_chunk = None

        # Step 1: Run image creation and validation
        async for chunk in super()._run_async_impl(ctx):
            last_chunk = chunk
            yield chunk

        image_path = None
        if last_chunk is not None:
            content_obj = getattr(last_chunk, "content", None)
            if content_obj and hasattr(content_obj, "parts"):
                for part in content_obj.parts:
                    text = getattr(part, "text", "").strip()
                    if not text:
                        continue

                    # Use regex to find any .png/.jpg filename or URL inside the text
                    # This regex looks for strings ending with .png or .jpg, optionally preceded by URL or path chars
                    matches = re.findall(r"(https?://\S+?\.(?:png|jpg))|([\w./\\-]+\.(?:png|jpg))", text, re.IGNORECASE)
                    
                    if matches:
                        # matches is a list of tuples from the regex groups, pick the non-empty one
                        for url_match, path_match in matches:
                            candidate = url_match or path_match
                            if candidate:
                                image_path = candidate
                                ctx.session.state["final_image"] = image_path
                                print("✅ Saved final_image:", image_path)
                                break
                    if image_path:
                        break

        # Step 2: If image_path exists, generate a caption using the same model
        if image_path:
            result = await self.generate_caption(image_path)
            ctx.session.state["image_caption"] = result.get("caption", "")
            ctx.session.state["image_content"] = result.get("content", "")
            print("✅ Saved image_caption:", ctx.session.state["image_caption"])
            print("✅ Saved image_content:", ctx.session.state["image_content"])



    async def generate_caption(self, image_path: str) -> str:
        """
        Return the following two statements clearly and separately in the output:
        
        1) Caption : Generate a single, concise, and descriptive caption that summarizes the overall theme and message of the image.

        2) Content : Describe the visual content of the image, including key objects, people, actions, or settings present.

        Ensure both are accurate and directly based on the image. Do not include any additional suggestions, hashtags, or explanations.
        """

        if not os.path.exists(image_path):
            return f"❌ Image not found at path: {image_path}"

        # Load the image as PIL Image
        image = Image.open(image_path)

        prompt_text = (
            "Return ONLY the following 2cls items clearly and separately:\n\n"
            "1) Caption : Generate a single, concise, and descriptive caption that summarizes the overall theme and message of the image.\n\n"
            "2) Content : Describe the visual content of the image, including key objects, people, actions, or settings present.\n\n"
            "Ensure both are accurate and directly based on the image. Do not include any additional suggestions, hashtags, or explanations."
            "Make sure to return only these 2 things in the output and nothing else, no other text, explanations or so"
        )

        try:
            response = client.models.generate_content(
                model="models/gemini-2.0-flash",  
                contents=[
                    prompt_text,
                    image
                ]
            )
        except Exception as e:
            return {"caption": "", "content": f"❌ Caption generation failed: {e}"}

        if not response.candidates:
            return {"caption": "", "content": "⚠️ No candidates returned by model."}

        raw_text = response.candidates[0].content.parts[0].text.strip()

        # Parse the output text to extract Caption and Content separately
        # This regex looks for "Caption : <text>" and "Content : <text>" parts, case insensitive
        caption_match = re.search(r"1\)?\s*Caption\s*:\s*(.*?)(?:\n{2,}|$)", raw_text, re.IGNORECASE | re.DOTALL)
        content_match = re.search(r"2\)?\s*Content\s*:\s*(.*)", raw_text, re.IGNORECASE | re.DOTALL)

        caption_text = caption_match.group(1).strip() if caption_match else ""
        content_text = content_match.group(1).strip() if content_match else ""

        return {
            "caption": caption_text,
            "content": content_text
        }


image_generation_agent = ImageGenerationAgent(
    name="image_generation_agent",
    model="gemini-2.0-flash",
    description=(
        "An agent that generates visuals based on the campaign narrative. "
        "It returns the path to the saved image file."
    ),
    instruction=(
        "Use the `image_creator` tool to generate an image from campaign text.\n"
        "Then validate the image with `image_checker` to ensure it's clean, relevant, and grammatically correct.\n"
        "Only return the path if image_checker passes.\n"
        "If not valid, regenerate using `image_creator` again."
        "Return the filepath to the saved image."
    ),
    tools=[image_creator, image_checker]
)

root_agent = image_generation_agent
