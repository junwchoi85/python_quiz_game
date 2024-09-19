# core/entities/question.py

class Question:
    def __init__(self, category, question_type, difficulty, question, correct_answer, incorrect_answers):
        self.category = category
        self.question_type = question_type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
