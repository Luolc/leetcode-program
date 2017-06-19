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
    def get_solved_questions():
        questions = LocalResource.get_questions()
        # Solved questions are which listed in '/res/solutions/' directory.
        solved_questions = list(map(lambda x: int(x), os.listdir(Constant.SOLUTIONS_PATH)))
        solved_questions = list(filter(lambda x: x['number'] in solved_questions, questions))
        return solved_questions

    @staticmethod
    def get_unsolved_questions():
        questions = LocalResource.get_questions()
        solved_questions = list(map(lambda x: int(x), os.listdir(Constant.SOLUTIONS_PATH)))
        unsolved_questions = list(filter(lambda x: x['number'] not in solved_questions, questions))
        return unsolved_questions
