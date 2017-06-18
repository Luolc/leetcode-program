import os
import inspect
import fire
import json
from spider import Spider

RES_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../res/'


class Main:
    @staticmethod
    def update_local_questions(js_path):
        print()
        # r'/usr/local/bin/phantomjs'
        questions = Spider(js_path=js_path).fetch_questions()
        with open(RES_PATH + 'leetcode-questions.json', 'w') as f:
            json.dump(questions, f, indent=2, sort_keys=True)

if __name__ == '__main__':
    fire.Fire(Main)
