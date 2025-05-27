def correct_and_optimize(narrative: str) -> str:
    return (
        f"Here is a draft campaign message:\n\n"
        f"{narrative}\n\n"
        f"Polish the content to make it clearer, more concise, emotionally resonant, and grammatically perfect.\n"
        f"Ensure it sounds natural and human.\n"
        f"Output ONLY the improved campaign narrative with NO explanations or comments."
    )
