import re
import random

responses = {
    'hello': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
    'how are you': ['I am doing well, thank you!', 'I am fine, how about you?', 'I am great, thanks for asking!'],
    'bye': ['Goodbye!', 'See you later!', 'Take care!'],
    'what is your name': ['I am a chatbot created by Python.', 'You can call me Chatbot!', 'My name is Python Bot!'],
    'default': ["I'm sorry, I don't understand.", "Can you say that again?", "Please tell me more."]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if re.search(r'\b' + key + r'\b', user_input):
            return random.choice(responses[key])
    return random.choice(responses['default'])

def chatbot():
    print("Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if 'bye' in user_input.lower():
            print("Chatbot: Goodbye! Have a nice day!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
