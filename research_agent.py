import json

class ResearchAgent:
    def __init__(self, filename="cafe_data.json"):
        self.menu_data = self.load_menu_data(filename)

    def load_menu_data(self, filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("❌ Error: 'cafe_data.json' not found.")
            return None

    def get_ingredients(self, drink_name):
      if not self.menu_data:
        return "❌ Menu data not loaded."

      drink = self.menu_data["menu"].get(drink_name)
      if not drink:
             return f"❌ '{drink_name}' is not on the menu."
      return drink["ingredients"]

    def get_nutrition(self, drink_name):
      if not self.menu_data:
           return "❌ Menu data not loaded."

      drink = self.menu_data["menu"].get(drink_name)
      if not drink:
             return f"❌ '{drink_name}' is not on the menu."
      return drink["nutrition"]


    def get_opening_hours(self, day):
        if not self.menu_data:
            return "❌ Menu data not loaded."

        hours = self.menu_data["opening_hours"].get(day)
        if not hours:
            return f"❌ Invalid day: {day}"
        return f"🕒 {day}'s Opening Hours: {hours}"

    def list_drinks(self):
        if not self.menu_data:
            return "❌ Menu data not loaded."

        return "🍹 Available Drinks:\n" + "\n".join(self.menu_data["drinks"])

