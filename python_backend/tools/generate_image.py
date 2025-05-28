import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

from dotenv import load_dotenv

load_dotenv()

def image_creator(campaign_text: str, style: str = "cheerful") -> str:
    prompt = (
    f"You are a visual design assistant. Your task is to generate a bold, clean, emotionally powerful image for a public awareness campaign.\n\n"

    f"🎯 **CAMPAIGN GOAL:** Visually express the following idea using {style} illustration style:\n"
    f"\"{campaign_text.strip()}\"\n\n"

    f"🚫 **STRICT RULES (DO NOT BREAK):**\n"
    f"1. ✏️ **Only One Tagline**\n"
    f"- Include **only ONE short, meaningful tagline** (5–10 words max).\n"
    f"- Must be **valid, grammatical English** with no spelling or syntax errors.\n"
    f"- Do **not** use special characters, emojis, broken words, or gibberish.\n"

    f"2. 💬 **Text Style & Placement**\n"
    f"- Text must be **bold, sans-serif, high contrast** and clearly readable.\n"
    f"- Place the tagline either **centered**, **top**, or **bottom** — never overlapping detailed artwork.\n"

    f"3. 🖼️ **Artwork Instructions**\n"
    f"- Use a clean, {style.lower()} digital illustration style.\n"
    f"- Show clear, relatable **urban family scenarios** like recycling, gardening, or biking.\n"
    f"- Avoid clutter, avoid surreal/abstract art.\n"

    f"4. 📵 **NO Extra Text**\n"
    f"- Do **not** include paragraphs, slogans, captions, logos, watermarks, or any secondary text.\n"
    f"- Only the tagline must appear in the image.\n"

    f"5. 📱 **Format**\n"
    f"- High-resolution, mobile-optimized, and social-media ready.\n"

    f"🔥 GOAL: A shareable, impactful visual with one clear, grammatically correct tagline — and nothing else."
)



    print("Prompt for image generation:")
    print(prompt)

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]
        )
    )

    print("Received response from image generation model.")
    print("Number of parts:", len(response.candidates[0].content.parts))

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "generated_image.png")

    text_found = None  # keep any text found, but continue to check for image

    for idx, part in enumerate(response.candidates[0].content.parts):
        print(f"Inspecting part {idx}:")
        print(" - inline_data:", part.inline_data is not None)
        print(" - text present:", part.text is not None)

        if part.inline_data is not None:
            try:
                image = Image.open(BytesIO(part.inline_data.data))
                image.save(output_path)
                print(f"Image successfully saved at {output_path}")
                return output_path
            except Exception as e:
                print("Exception while saving image:", e)
                return f"Image saving failed: {e}"
        elif part.text is not None:
            print("Received text instead of image:", part.text)
            text_found = part.text  # store text but don't return immediately

    if text_found:
        return text_found

    return "Image generation failed: No image or text parts found."




image_creator("Let's make our city a greener, cleaner place for all! Our new recycling initiative makes it easier than ever to recycle right. Imagine a future with less waste in landfills and more resources for our community. Join us in making a real difference, one bin at a time!")