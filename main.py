def chatbot():
    print("Welcome to chatbot")
    print("Type 'exit' to stop.")

    while True:
        user_input = input("You:")

        if user_input.lower() == "exit":
            print("Chatbot:Goodbye")
            break

        print("Chatbot: You said:", user_input)

if __name__ == "__main__":
    chatbot() 