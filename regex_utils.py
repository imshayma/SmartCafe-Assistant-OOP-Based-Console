import json
import re
 
def detect_intent(user_input):
    # Normalize input
    user_input = user_input.lower()

    # Ingredient intent
    match = re.search(r"what\'s in (.+)|ingredients of (.+)", user_input)
    if match:
        drink = match.group(1) or match.group(2)
        return "ingredients", drink.title()

    # Nutrition intent
    match = re.search(r"calories in (.+)|nutrition of (.+)", user_input)
    if match:
        drink = match.group(1) or match.group(2)
        return "nutrition", drink.title()

    # Hours intent
    match = re.search(r"open on (.+)", user_input)
    if match:
        day = match.group(1).capitalize()
        return "hours", day

    # List drinks intent
    if re.search(r"what drinks do you have|available drinks|show menu", user_input):
        return "drinks", None

    return None, None
