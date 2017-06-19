import os
import inspect


class Constant:
    RES_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../res/'
    QUESTIONS_PATH = RES_PATH + 'leetcode-questions.json'
