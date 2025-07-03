import json

class ResearchAgent:
    def __init__(self):
        with open("cafe_data.json", "r") as file:
            self.data = json.load(file)

    def get_ingredients(self, drink):
        return self.data.get("ingredients", {}).get(drink.title(), "Not found")

    def get_nutrition(self, item):
        return self.data.get("nutrition", {}).get(item.title(), "Not found")

    def get_hours(self, day):
        return self.data.get("hours", {}).get(day.title(), "Not found")

    def get_drink_list(self):
        return list(self.data.get("ingredients", {}).keys())
