from research_agent import ResearchAgent
from regex_utils import detect_intent
from output_utils import format_output

class ChatBotAgent:
    def __init__(self):
        self.research_agent = ResearchAgent()

    def respond(self, user_input):
        intent, value = detect_intent(user_input)

        if intent == "ingredients":
          result = self.research_agent.get_ingredients(value)
          if isinstance(result, list):
             return f"🧾 Ingredients in {value}: " + ", ".join(result)
          return result

        elif intent == "nutrition":
           result = self.research_agent.get_nutrition(value)
           if isinstance(result, dict):
               return f"📊 {value} - Calories: {result['calories']} kcal, Sugar: {result['sugar_g']}g"
           return result

        elif intent == "hours":
           return self.research_agent.get_opening_hours(value)

        elif intent == "drinks":
            return self.research_agent.list_drinks()

        else:
            return "❌ I'm sorry, I didn't understand your question."

# Optional testing block
if __name__ == "__main__":
    bot = ChatBotAgent()
    print("👋 Welcome to SmartCafe Assistant! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = bot.respond(user_input)
        print(response)
