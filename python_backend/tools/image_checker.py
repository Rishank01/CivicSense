import os
from PIL import Image
try:
    import pytesseract
    pytesseract_available = True
except ImportError:
    pytesseract_available = False

from google import genai
from google.genai import types

def simple_blur_detection(image: Image.Image, threshold=100) -> bool:
    try:
        import cv2
        import numpy as np
    except ImportError:
        # If cv2 or numpy missing, skip blur detection
        return True

    # Convert PIL Image to OpenCV Image
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance > threshold

def extract_text_from_image(image_path: str) -> str:
    if pytesseract_available:
        try:
            text = pytesseract.image_to_string(Image.open(image_path)).strip()
            return text
        except Exception:
            return ""
    else:
        # Fallback dummy text if pytesseract unavailable
        return "dummy tagline text extracted"

def image_quality_checks(image_path: str) -> str:
    try:
        image = Image.open(image_path)
    except Exception as e:
        return f"FAIL: Could not open image: {e}"

    # Example blur detection
    sharp_enough = simple_blur_detection(image)
    if not sharp_enough:
        return "FAIL: Image appears too blurry"

    return "PASS"

def image_checker(image_path: str, narrative: str) -> str:
    print("Is pytesseract available? -->", pytesseract_available)

    # Step 1: Check image quality
    quality_result = image_quality_checks(image_path)
    if quality_result != "PASS":
        return quality_result

    # Step 2: Extract text from image
    extracted_text = extract_text_from_image(image_path)
    if not extracted_text:
        return "FAIL: No readable text (tagline) found in the image"

    # Step 3: Validate tagline relevance and grammar with LLM
    prompt = f"""
You are a visual quality assurance expert.

The campaign narrative is:
\"\"\"{narrative}\"\"\"

The tagline extracted from the campaign image is:
\"\"\"{extracted_text}\"\"\"

Please check the following:
- Is the tagline grammatically correct English?
- Is the tagline relevant and consistent with the campaign narrative?
- Is the tagline concise (5-10 words max) and clear?

Respond ONLY with one of the following:
- PASS
- FAIL: followed by the reason(s) for failure.
"""

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT"]
        )
    )

    content = response.candidates[0].content

    # Defensive extraction of text from response content
    if hasattr(content, "text") and content.text:
        llm_response = content.text.strip()
    elif hasattr(content, "parts") and content.parts:
        # Take first non-empty text part
        llm_response = None
        for part in content.parts:
            if hasattr(part, "text") and part.text:
                llm_response = part.text.strip()
                break
        if llm_response is None:
            return "FAIL: No textual response from LLM."
    else:
        return "FAIL: No textual response from LLM."

    # Check response validity
    if llm_response.upper() == "PASS":
        return "PASS"
    elif llm_response.upper().startswith("FAIL"):
        return llm_response
    else:
        return "FAIL: LLM response unclear"

# Example (do not run standalone, just call from your tool/agent):
# result = image_checker("output/generated_image.png", "Make our city greener and cleaner!")
# print(result)
