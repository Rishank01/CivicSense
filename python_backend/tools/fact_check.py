def fact_check(narrative: str) -> str:
    return (
        f"Fact check the following narrative for accuracy:\n\n"
        f"{narrative}\n\n"
        f"Reply with a brief report if any facts are incorrect, outdated, or need citations.\n"
        f"If all facts are accurate, reply ONLY: 'All facts verified.'\n"
        f"Do NOT include additional comments."
    )
