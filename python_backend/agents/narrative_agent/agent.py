# agent.py or main.py
from google.adk import Agent
from tools.generate_narrative import generate_narrative
from tools.correct_and_optimize import correct_and_optimize
from tools.fact_check import fact_check
from tools.validate_output import validate_output


class NarrativeAgent(Agent):
    async def _run_async_impl(self, ctx):
        print("Inside the function")
        last_chunk = None

        async for chunk in super()._run_async_impl(ctx):
            last_chunk = chunk
            yield chunk

        if last_chunk is not None:
            print("Last chunk object:", last_chunk)
            content_obj = getattr(last_chunk, "content", None)
            print("Last chunk content:", content_obj)

            if content_obj is not None and hasattr(content_obj, "parts"):
                # Extract text from the first part
                for part in content_obj.parts:
                    text_str = getattr(part, "text", None)
                    if text_str:
                        ctx.session.state["final_narrative"] = text_str.strip()
                        print("✅ Saved final_narrative:", ctx.session.state["final_narrative"])
                        break
                else:
                    print("❌ No text found in any content parts.")
            else:
                print("❌ Content object is missing or doesn't have parts.")
        else:
            print("❌ No chunk was yielded from the agent.")



narrative_agent = NarrativeAgent(
    name="narrative_agent",
    model="gemini-2.0-flash",
    description="A reasoning agent that decides when to generate, correct, fact-check, and validate campaign narratives.",
    instruction=(
        "You are a smart content strategist. Based on the summary, tone if provided otherwise persuasive, and audience if provided otherwise nation wide, "
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

