from research_agent import ResearchAgent
from regex_utils import detect_intent
from output_utils import format_output

class ChatBotAgent:
    def __init__(self):
        self.research_agent = ResearchAgent()

    def respond(self, user_input):
        intent, item = detect_intent(user_input)
        if intent == "ingredient":
            return format_output("Ingredients", self.research_agent.get_ingredients(item))
        elif intent == "nutrition":
            return format_output("Nutrition", self.research_agent.get_nutrition(item))
        elif intent == "hours":
            return format_output("Hours", self.research_agent.get_hours(item))
        elif intent == "list":
            return format_output("Drinks", self.research_agent.get_drink_list())
        else:
            return "Sorry, I didn't understand that."