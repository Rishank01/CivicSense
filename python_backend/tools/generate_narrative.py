def generate_narrative(summary: str, tone: str = "informative", audience: str = "general public") -> str:
    if not summary:
        return "No summary provided."

    return (
        f"You are a talented human storyteller creating a {tone} campaign message for {audience}.\n\n"
        f"Summary:\n\"{summary}\"\n\n"
        f"Write a clear, detailed, cheerful, and emotionally engaging narrative, especially suited for {audience}. "
        f"Make it friendly, fun, and inspiring. Use vivid imagery, examples, or a little story to make it memorable.\n\n"
        f"**Important**: Only return the final narrative — do NOT add introductions, instructions, or notes."
    )
