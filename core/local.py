import json
import os
from constant import Constant


class LocalResource:
    @staticmethod
    def get_questions():
        with open(Constant.QUESTIONS_PATH, 'r') as f:
            questions = json.load(f)
        return questions

    @staticmethod
    def get_question(number):
        return next(q for q in LocalResource.get_questions() if q['number'] == number)

    @staticmethod
    def get_solved_questions():
        questions = LocalResource.get_questions()
        # Solved questions are which listed in '/res/solutions/' directory.
        # map(lambda x:x+2, [1, 2, 3])  ----->  [3, 4, 5]
        try:
            solved_questions = list(map(lambda x: int(x), os.listdir(Constant.SOLUTIONS_PATH)))
        except FileNotFoundError:
            solved_questions = []

        solved_questions = list(filter(lambda q: q['number'] in solved_questions, questions))
        return solved_questions

    @staticmethod
    def get_unsolved_questions():
        questions = LocalResource.get_questions()
        solved_questions = list(map(lambda q: q['number'], LocalResource.get_solved_questions()))
        unsolved_questions = list(filter(lambda q: q['number'] not in solved_questions, questions))
        return unsolved_questions
