from google import genai
from PIL import Image
import os
from dotenv import load_dotenv
import re

load_dotenv()

# Initialize the ADK-compatible client
client = genai.Client()

def load_image(image_path: str):
    """
    Loads an image from a local file path and returns a PIL Image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    return Image.open(image_path)

def generate_caption(image_path: str) -> str:
    """
    Return the following two statements clearly and separately in the output:
    
    1) Caption : Generate a single, concise, and descriptive caption that summarizes the overall theme and message of the image.

    2) Content : Describe the visual content of the image, including key objects, people, actions, or settings present.

    Ensure both are accurate and directly based on the image. Do not include any additional suggestions, hashtags, or explanations.
    """
    image = load_image(image_path)

    prompt_text = (
        "Return ONLY the following 2cls items clearly and separately:\n\n"
        "1) Caption : Generate a single, concise, and descriptive caption that summarizes the overall theme and message of the image.\n\n"
        "2) Content : Describe the visual content of the image, including key objects, people, actions, or settings present.\n\n"
        "Ensure both are accurate and directly based on the image. Do not include any additional suggestions, hashtags, or explanations."
        "Make sure to return only these 2 things in the output and nothing else, no other text, explanations or so"
    )

    response = client.models.generate_content(
        model="models/gemini-2.0-flash",  # or "models/gemini-2.5-flash-preview"
        contents=[
            prompt_text,
            image
        ]
    )

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


# Example usage
if __name__ == "__main__":
    path = r"output\generated_image.png"  # Use raw string or forward slashes
    caption_and_content = generate_caption(path)
    print(caption_and_content.get("caption", ""))
    print(caption_and_content.get("content", ""))
    print(caption_and_content)
