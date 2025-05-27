from google.adk import Agent
from tools.generate_image import generate_image

image_generation_agent = Agent(
    name="image_generation_agent",
    model="gemini-2.0-flash",
    description="An agent that generates visual prompts based on the final campaign narrative.",
    instruction=(
        "You are a creative visual designer agent. Your task is to generate a vivid image prompt "
        "that aligns with the provided campaign text. Consider the emotional tone and audience.\n\n"
        "Use the `generate_image` tool with the final campaign narrative as input.\n"
        "Return only the image prompt description. Do not explain your reasoning."
    ),
    tools=[generate_image]
)

root_agent = image_generation_agent
