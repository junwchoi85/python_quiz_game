# interfaces/cli/game_controller.py

from core.usecases.play_game import PlayGame
from data import question_data
from core.entities.question import Question
import random


def load_questions():
    questions = []
    global question_data
    # Randomly select 10 questions from the question_data
    # and create a Question object for each question
    random.shuffle(question_data)
    question_data = question_data[:10]
    for q_data in question_data:
        q = Question(
            q_data['category'],
            q_data['type'],
            q_data['difficulty'],
            q_data['question'],
            q_data['correct_answer'],
            q_data['incorrect_answers']
        )
        questions.append(q)
    return questions


def start_game():
    questions = load_questions()
    game = PlayGame(questions)
    game.start()
