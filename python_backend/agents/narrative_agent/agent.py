# agent.py or main.py
from google.adk import Agent
from tools.generate_narrative import generate_narrative
from tools.correct_and_optimize import correct_and_optimize
from tools.fact_check import fact_check
from tools.validate_output import validate_output

narrative_agent = Agent(
    name="narrative_agent",
    model="gemini-2.0-flash",
    description="A reasoning agent that decides when to generate, correct, fact-check, and validate campaign narratives.",
    instruction=(
        "You are a smart content strategist. Based on the summary, tone, and audience provided, "
        "use the available tools to generate a compelling narrative. Then decide whether it needs correction, "
        "fact checking, or validation. Continue using tools as needed until the narrative is polished and ready.\n\n"
        "Use `generate_narrative` only once per task. After that, improve or verify the output using other tools.\n"
        "Finish when the output passes validation.\n"
        "IMPORTANT: Output ONLY the final campaign narrative directly — no intros, no comments, no explanation."
    ),
    tools=[
        generate_narrative,
        correct_and_optimize,
        fact_check,
        validate_output
    ]
)

root_agent = narrative_agent

