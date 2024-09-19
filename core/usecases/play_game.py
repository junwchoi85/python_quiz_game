# core/usecases/play_game.py

import random


class PlayGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        print(f"Category: {question.category}")
        print(f"Question: {question.question}")
        answer = input("Your answer (True/False): ").strip()
        # let the user input either 'True' or 'False' and convert it to lowercase
        answer = answer.lower()
        # Also accept 'T' or 'F' as input
        if answer == 't':
            answer = 'true'
        elif answer == 'f':
            answer = 'false'

        if answer == question.correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was {question.correct_answer}\n")

    def start(self):
        print("Welcome to the Question Game!")
        random.shuffle(self.questions)
        for q in self.questions:
            self.ask_question(q)
        print(f"Game Over! Your final score is: {self.score}")
