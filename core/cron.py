import random
from github import GitHubClient
from constant import Constant
from local import LocalResource


class Cron:
    def __init__(self, token):
        self.__github__ = GitHubClient(Constant.USERNAME, token)

    def create_daily_task(self):
        unsolved_questions = LocalResource.get_unsolved_questions()
        pending_questions = self.__github__.get_task_issue_question_numbers()
        unsolved_questions = list(filter(lambda q: q['number'] not in pending_questions, unsolved_questions))

        easy_questions = list(filter(lambda q: q['difficulty'] == 'Easy', unsolved_questions))
        medium_questions = list(filter(lambda q: q['difficulty'] == 'Medium', unsolved_questions))
        hard_questions = list(filter(lambda q: q['difficulty'] == 'Hard', unsolved_questions))
        random.shuffle(easy_questions)
        random.shuffle(medium_questions)
        random.shuffle(hard_questions)

        issues = []
        issues += [
            self.__github__.create_task_issue(q['number']) for q in easy_questions[0:Constant.CRON_CONFIG['Easy']]
        ]
        issues += [
            self.__github__.create_task_issue(q['number']) for q in medium_questions[0:Constant.CRON_CONFIG['Medium']]
        ]
        issues += [
            self.__github__.create_task_issue(q['number']) for q in hard_questions[0:Constant.CRON_CONFIG['Hard']]
        ]
        return issues
