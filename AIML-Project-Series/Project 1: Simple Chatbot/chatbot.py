import random
from fuzzywuzzy import fuzz
#Color codes
CYAN = "\033[96m"
MAGENTA = "\033[95m"
ORANGE = "\033[93m"
LIGHT_GREEN = "\033[92m"
LIGHT_RED = "\033[91m"
RESET = "\033[0m"

class SerenAI:
    def __init__(self):
        self.user_name = ""
        self.context = {}

    def greet(self):
        print(f"{LIGHT_GREEN}\nHello Human! 👋 \nI am SerenAI, Your Friendly Chatbot.")

    def goodbye(self):
        print(f"{CYAN}\nGoodbye! 👋 \nIf you have more questions, feel free to ask.{RESET}")

    def get_similarity(self, input_str, target_str):
        return fuzz.ratio(input_str.lower(), target_str.lower())

    def handle_question(self, question):
        if self.get_similarity(question, "hi") >= 80:
            response = "Hello! How can I help you today?"

        elif self.get_similarity(question, "my name") >= 80:
            response = f"I remember your name! You are {self.context.get('user_name', 'a stranger')}."

        elif "what is my" in question:
            # Strip "what is my" from the question
            key = question.replace("what is my", "").strip()
            # Check if the remaining part matches any context key
            found = False
            for context_key, value in self.context.items():
                if self.get_similarity(key, context_key) >= 80:
                    response = f"Your {key} is {value}."
                    found = True
                    break
            if not found:
                response = f"{MAGENTA}I don't know your {key}. Could you please tell me?{RESET}"


        elif self.get_similarity(question, 'who are you') >= 80:
            response = "I'm a SerenAI, Just a simple Chatbot."
        elif self.get_similarity(question, 'what can you do') >= 80:
            response = "I can answer your questions and engage in simple conversations."
        elif self.get_similarity(question, 'how are you') >= 80:
            response = "I'm computer program, I dont have feelings but thanks for asking! 😊"
        elif self.get_similarity(question, 'tell me a joke') >= 80:
            jokes = [
                "Why did the computer go to therapy? It had too many bytes of emotional baggage.",
                "Why was the math book sad? Because it had too many problems.",
                "I told my computer I needed a break, and now it won't stop sending me vacation ads.",
                "Why don't oysters donate to charity? Because they are shellfish.",
                "I used to be a baker because I kneaded dough.",
                "I told my wife she should embrace her mistakes. She gave me a hug."
            ]
            response = random.choice(jokes)
        elif self.get_similarity(question, 'exit') >= 80:
            self.goodbye()
            exit()
        else:
            response = f"{MAGENTA}I'm sorry, I didn't understand that. Can you please ask another question? or do you want to exit?{RESET}"
        return response

    def ask_name(self):
        self.user_name = input(f"{ORANGE}Bot: What is your name? {RESET}")
        if self.user_name:
            self.context['user_name'] = self.user_name
            print(f"{LIGHT_GREEN}Bot: Nice to meet you, {self.user_name}!{RESET}")
        else:
            print(f"{LIGHT_RED}Bot: I didn't catch your name. Please try again.{RESET}")
            self.ask_name()

    def ask_personal_questions(self):
        questions = [
            "What is your favorite color?",
            "What is your favorite hobby?",
            "What is your favorite food?",
            "What is your favorite movie?"
        ]
        for question in questions:
            response = input(f"{ORANGE}Bot: {question} {RESET}")
            self.context[question.lower().replace("what is your ", "").replace("?", "")] = response

    def chat(self):
        self.greet()
        self.ask_name()
        self.ask_personal_questions()

        while True:
            print("Feel free to ask any questions!")
            user_input = input(f"{ORANGE}You: {RESET}").lower()
            user_input = user_input.strip(",.?/'}{!@#$%^&*()")
            response = self.handle_question(user_input)
            print(f"{LIGHT_GREEN}Bot: {RESET}{response}")

        

if __name__ == "__main__":
    bot = SerenAI()
    bot.chat()
