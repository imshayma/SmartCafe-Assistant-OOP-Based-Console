from chatbot_agent import ChatBotAgent

def main():
    bot = ChatBotAgent()
    print("Welcome to SmartCafe ☕ How can I help you today?")
    while True:
        user_input = input(">> ").strip().lower()
        if user_input in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = bot.respond(user_input)
        print(response)

if __name__ == "__main__":
    main()
