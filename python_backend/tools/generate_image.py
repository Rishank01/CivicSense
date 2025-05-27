# tools/generate_image.py

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

def image_creator(campaign_text: str, style: str = "cheerful") -> str:
    """
    Generate an image using Gemini-2.0-flash-preview-image-generation based on campaign text.
    """
    # Keep prompt short and safe
    prompt = (
        f"Create a {style} digital illustration that visually represents this campaign message:\n\n"
        f"{campaign_text.strip()[:300]}\n\n"
        f"The image should be suitable for social media and resonate with urban families."
    )

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"]
        )
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            image.save("generated_image.png")
            return "Image saved as generated_image.png"
        elif part.text is not None:
            return part.text

    return "Image generation failed."
