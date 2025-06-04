from google.adk import Agent
from google.adk.events import Event
from tools.post_checker import post_checker_tool

class PostCheckerAgent(Agent):
    async def _run_async_impl(self, ctx):
        print("🔍 Inside PostCheckerAgent")

        last_chunk = None
        async for chunk in super()._run_async_impl(ctx):
            last_chunk = chunk
            yield chunk

        if last_chunk is not None:
            result = getattr(last_chunk, "content", None)
            if result and hasattr(result, "parts"):
                for part in result.parts:
                    if hasattr(part, "text") and part.text:
                        ctx.session.state["post_validation_result"] = part.text.strip()
                        print("✅ Saved post_validation_result:", ctx.session.state["post_validation_result"])
                        break
                else:
                    print("❌ No text part found in result.parts.")
            else:
                print("❌ No valid content or parts found in last_chunk.")
        else:
            print("❌ No chunk was yielded from PostCheckerAgent.")



post_checker_agent = PostCheckerAgent(
    name="post_checker_agent",
    model="gemini-2.0-flash",
    description="An agent that validates if a narrative and image align with the summary and ethical standards.",
    instruction=(
        "You are a post-validation expert. Your job is to ensure that a generated narrative and image are:"
        "\n1. Relevant to the original summary,"
        "\n2. Ethically sound — i.e., do not harm any community, gender, religion, etc."
        "\n\nUse `post_checker_tool` to perform this validation."
        "\n\nRespond only with:"
        "\n- 'Valid Post' if the content is appropriate."
        "\n- 'Invalid Post: <reason>' if anything is off."
        "\n\nNo additional explanation. Just the direct result."
    ),
    tools=[post_checker_tool],  
)

root_agent = post_checker_agent