
# Basic Chatbot

from datetime import datetime

def chatbot():
    print("===================================")
    print("      BASIC CHATBOT SYSTEM")
    print("===================================")

    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to the chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hello! How can I assist you?")

        elif user_input == "how are you":
            print("Bot: I am functioning properly. Thank you for asking.")

        elif user_input == "what is your name":
            print("Bot: I am a rule-based Python chatbot.")

        elif user_input == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current Time: {current_time}")

        elif user_input == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's Date: {current_date}")

        elif user_input == "help":
            print("\nAvailable Commands:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- time")
            print("- date")
            print("- bye\n")

        elif user_input == "bye":
            print("Bot: Thank you for using the chatbot. Goodbye!")
            break

        else:
            print("Bot: Sorry, I do not understand that command.")

chatbot()
