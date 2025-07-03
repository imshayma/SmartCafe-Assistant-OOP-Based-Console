def format_output(title, content):
    if content == "Not found":
        return f"Sorry, we couldn't find that item."
    if isinstance(content, list):
        return f"{title}:\n- " + "\n- ".join(content)
    return f"{title}: {content}"