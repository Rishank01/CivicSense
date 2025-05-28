import os
from google.adk.agents import SequentialAgent
from agents.narrative_agent.agent import narrative_agent
from agents.image_generation_agent.agent import image_generation_agent

post_generation_pipeline = SequentialAgent(
    name="CampaignPostGenerator",
    description="Generates narrative and image using sub-agents in sequence.",
    sub_agents=[
        narrative_agent,
        image_generation_agent
    ]
)

root_agent = post_generation_pipeline

# async def run_post_generation_no_state():
#     context = {}

#     # Run narrative agent
#     narrative_response = await narrative_agent.run_async(context)
#     narrative_text = ""
#     async for event in narrative_response:
#         if event.content and event.content.parts:
#             narrative_text = event.content.parts[0].text
#             break

#     # Pass narrative to image generation agent
#     context["campaign_text"] = narrative_text

#     # Run image generation agent
#     image_response = await image_generation_agent.run_async(context)
#     image_path = None
#     async for event in image_response:
#         if event.content and event.content.parts:
#             part = event.content.parts[0]
#             if part.text:
#                 image_path = part.text
#                 break

#     # Return combined final response dict
#     return {
#         "narrative": narrative_text,
#         "image_path": image_path or "No image generated"
#     }


