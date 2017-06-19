import fire
import json
from spider import Spider
from cron import Cron
from constant import Constant


class Main:
    @staticmethod
    def update_local_questions(js_path):
        # r'/usr/local/bin/phantomjs'
        questions = Spider(js_path=js_path).fetch_questions()
        with open(Constant.QUESTIONS_PATH, 'w') as f:
            json.dump(questions, f, indent=2, sort_keys=True)

    @staticmethod
    def create_daily_task(token):
        Cron(token).create_daily_task()

if __name__ == '__main__':
    fire.Fire(Main)
