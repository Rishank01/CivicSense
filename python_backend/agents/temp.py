from PIL import Image
import pytesseract
from imageio import imread

# Test image path (replace with a valid image path on your system)
image_path = 'test_image.png'

try:
    # Load image using PIL
    image = Image.open(image_path)

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)
    print("Extracted Text:")
    print(text)
except Exception as e:
    print("Error occurred:", e)
