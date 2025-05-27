# agents/image_generation_agent/agent.py

from google.adk import Agent
from tools.generate_image import image_creator  # renamed function

image_generation_agent = Agent(
    name="image_generation_agent",
    model="gemini-2.0-flash",
    description="An agent that generates visuals based on the final campaign narrative.",
    instruction=(
        "You are a creative visual designer. When given a campaign text, use the `image_creator` tool to generate a vivid image. "
        "After generating the image, respond with a confirmation like 'Image generation complete.' Do not call the tool again."
    ),
    tools=[image_creator]
)

root_agent = image_generation_agent
