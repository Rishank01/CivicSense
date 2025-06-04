from google.adk.agents import LoopAgent, BaseAgent
from google.adk.events import Event, EventActions
from agents.narrative_agent.agent import narrative_agent
from agents.image_generation_agent.agent import image_generation_agent
from agents.post_checker_agent.agent import post_checker_agent
from pydantic import Field
from typing import Any


class PostValidityCheckerAgent(BaseAgent):
    """
    Custom agent to check session state for validation result and escalate if valid.
    """
    async def _run_async_impl(self, ctx):
        last_result = ctx.session.state.get("post_validation_result", "")
        is_valid = last_result.strip().lower().startswith("valid post")

        print(f"🔎 Checking post validity: {last_result}")
        yield Event(author=self.name, actions=EventActions(escalate=is_valid))


class PostGenerationRetryLoop(LoopAgent):
    """
    Custom LoopAgent that stores input summary in session state.
    """
    async def _run_async_impl(self, ctx):
        input_summary = getattr(ctx.session, "input", None)

        if input_summary and "input_summary" not in ctx.session.state:
            ctx.session.state["input_summary"] = input_summary
            print("✅ Saved input_summary to context:", input_summary)
        elif not input_summary:
            print("⚠️ No input found in ctx.session")

        async for chunk in super()._run_async_impl(ctx):
            yield chunk


class AsyncGeneratorWrapper(BaseAgent):
    """
    Wraps an agent and yields events from it, ensuring Pydantic-compatible content.
    """
    agent: Any = Field(..., description="The agent to wrap")

    def __init__(self, agent: Any, **kwargs):
        super().__init__(agent=agent, **kwargs)

    async def _run_async_impl(self, ctx):
        async for event in self.agent.run_async(ctx):
            # Expecting event.content as dict with key `validation_result`
            if isinstance(event.content, dict):
                ctx.session.state["post_validation_result"] = event.content.get("validation_result", "")
            else:
                ctx.session.state["post_validation_result"] = str(event.content)

            yield event


# Final loop agent
post_generation_loop = PostGenerationRetryLoop(
    name="PostGenerationRetryLoop",
    description="Retries narrative → image → validation until a valid post is generated or max attempts exhausted.",
    max_iterations=3,
    sub_agents=[
        narrative_agent,
        image_generation_agent,
        AsyncGeneratorWrapper(agent=post_checker_agent, name="PostCheckerWrapper"),
        PostValidityCheckerAgent(name="PostValidityChecker")
    ]
)

# Entry point
root_agent = post_generation_loop
