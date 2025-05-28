from google.adk import Agent
from tools.generate_image import image_creator
from tools.image_checker import image_checker

image_generation_agent = Agent(
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
