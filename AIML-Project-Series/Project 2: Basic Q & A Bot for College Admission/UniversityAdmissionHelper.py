import random
from datetime import datetime
from fuzzywuzzy import fuzz

# ANSI escape codes for text colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

class UniversityAdmissionsHelper:
    def __init__(self):
        self.user_info = {"name": "", "interest": ""}
        self.known_questions = {
            "admission requirements": "The admission requirements include a completed application form, your high school transcripts, SAT or ACT scores, and two letters of recommendation.",
            "admission deadline": "The application deadline for Fall 2024 is May 1st.",
            "application fee": "The application fee is $50, non-refundable.",
            "scholarships available": "We offer a range of scholarships based on academic merit and financial need. For more details, visit our scholarships page.",
            "undergraduate programs": "We offer a variety of undergraduate programs including Business, Engineering, Sciences, Arts, and Humanities. For a full list, please check our undergraduate programs catalog on our website.",
            "campus tours": "Campus tours are available every weekday at 10 AM and 2 PM. Special arrangements can be made for weekend tours if contacted in advance.",
            "student housing": "We have several student housing options ranging from dormitories to shared apartments. For more information, visit our housing section on the website.",
            "international students": "International students are required to submit additional documents including proof of English language proficiency, a copy of their passport, and financial support documents. For a detailed checklist, please see our international admissions guide.",
            "online courses": "Yes, we offer a range of online courses and degree programs. For more information, please visit our online education portal.",
            "transfer students": "Transfer students are welcome! You'll need to submit your transcripts from previous institutions and a transfer application. Some programs may have additional requirements."
        }

    def greet_user(self):
        print(f"{YELLOW}Hello! I'm the College Admission Bot. What's your name?{RESET}")
        self.user_info["name"] = input("> ")
        print(f"{GREEN}Nice to meet you, {self.user_info['name']}! How can I help you with your college admission today?{RESET}")

    def get_similarity(self, input_str, target_str):
        return fuzz.ratio(input_str.lower(), target_str.lower())

    def handle_query(self, query):
        if "again" in query and self.user_info["interest"]:
            response = self.known_questions.get(self.user_info["interest"], "Could you specify the topic again?")
            print(f"{BLUE}{response}{RESET}")
            return

        best_match = None
        highest_similarity = 0

        for key in self.known_questions:
            similarity = self.get_similarity(query, key)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = key

        if highest_similarity > 70:  # Setting a threshold for matching
            response = self.known_questions[best_match]
            self.user_info["interest"] = best_match
            print(f"{BLUE}{response}{RESET}")
        else:
            print(f"{MAGENTA}I'm sorry, I don't have information on that. Can you ask something else?{RESET}")

    def personalized_response(self, query):
        if "my name" in query:
            response = f"Your name is {self.user_info['name']}."
            print(f"{BLUE}{response}{RESET}")
        elif "my interest" in query:
            if self.user_info["interest"]:
                response = f"Your current topic of interest is {self.user_info['interest']}."
            else:
                response = "You haven't mentioned any specific interests yet."
            print(f"{BLUE}{response}{RESET}")
        else:
            self.handle_query(query)

    def chat(self):
        self.greet_user()
        while True:
            query = input(f"{YELLOW}> {RESET}").lower()
            if query == "quit":
                print(f"{RED}Thanks for chatting. Goodbye!{RESET}")
                break
            else:
                self.personalized_response(query)

if __name__ == "__main__":
    bot = UniversityAdmissionsHelper()
    bot.chat()
