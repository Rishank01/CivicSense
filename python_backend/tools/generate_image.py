# from google.adk import tool

# @tool
def generate_image(campaign_text: str, style: str = "cheerful") -> str:
    """
    Generate an image prompt based on the campaign text and visual style.
    The result is an image description prompt suitable for a model like DALL·E or Gemini.

    Args:
        campaign_text (str): The final narrative for the campaign.
        style (str): Optional tone/style like 'cheerful', 'informative', 'dramatic'.

    Returns:
        str: An image prompt to be passed to an image generation model.
    """
    return (
        f"Create a {style} digital illustration that visually represents this campaign message:\n\n"
        f"\"{campaign_text}\"\n\n"
        f"Make the image suitable for social media, easy to understand by the target audience, and emotionally resonant."
    )
