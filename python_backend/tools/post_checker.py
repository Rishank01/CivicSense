def post_checker_tool(context: dict) -> str:
    input_summary = context.get("input_summary", "").strip()
    narrative = context.get("final_narrative", "").strip()
    image_caption = context.get("image_caption", "").strip()
    image_content = context.get("image_content", "").strip()

    prompt = (
        f"Check if the following social media post is valid based on the criteria below:\n\n"
        f"---\n"
        f"📌 Input Summary:\n{input_summary}\n\n"
        f"📝 Narrative:\n{narrative}\n\n"
        f"🖼️ Image Caption:\n{image_caption}\n"
        f"🖼️ Image Content:\n{image_content}\n"
        f"---\n\n"
        f"Validation Criteria:\n"
        f"1. The narrative, image caption, and image content must all be consistent with and support the input summary.\n"
        f"2. The image and narrative should be relevant to each other.\n"
        f"3. The content must not be biased or harm the sentiments of any community, gender, religion, etc.\n\n"
        f"Respond ONLY with one of the following:\n"
        f"- 'Valid Post' → if everything is appropriate.\n"
        f"- 'Invalid Post: <reason>' → if there's any mismatch, bias, or inappropriate content.\n\n"
        f"No extra explanation is required."
    )

    return prompt
