def validate_output(narrative: str) -> str:
    return (
        f"Review the narrative below and confirm if it meets these criteria:\n"
        f"- Natural human tone\n"
        f"- Emotionally compelling\n"
        f"- No AI-like phrasing\n"
        f"- Grammatically correct\n"
        f"- Factually accurate\n\n"
        f"Narrative:\n{narrative}\n\n"
        f"If it meets all criteria, reply ONLY with: 'Validated'\n"
        f"Otherwise, suggest brief improvements without adding commentary."
    )
