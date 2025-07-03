import re

def detect_intent(user_input):
    # Pattern examples
    if re.search(r"\bwhat's in\b|\bingredients\b", user_input):
        drink = re.findall(r"mocha|latte|.*", user_input)
        return "ingredient", drink[0] if drink else None
    elif re.search(r"\bcalories\b|\bnutrition\b", user_input):
        item = re.findall(r"hot chocolate|.*", user_input)
        return "nutrition", item[0] if item else None
    elif re.search(r"\bopen\b|\bhours\b", user_input):
        day = re.findall(r"monday|tuesday|friday|.*", user_input)
        return "hours", day[0] if day else None
    elif re.search(r"\bdrinks\b|\bmenu\b", user_input):
        return "list", None
    else:
        return None, None
