import requests
import re
from local import LocalResource


class GitHubClient:
    __BASE_URL__ = 'https://api.github.com/'

    __ISSUES_URL__ = __BASE_URL__ + 'repos/{}/leetcode-program/issues'

    __ISSUE_TITLE__ = '[Task] NO.{}: {}'

    __ISSUE_TITLE_REGEX__ = r'^\[Task\] NO\.([0-9]+):.+$'

    __ISSUE_BODY__ = 'Question link: {}'

    def __init__(self, username, token=''):
        self.__username__ = username
        self.__token__ = token
        self.__headers__ = {
            'User-Agent': username,
            'Authorization': 'token {}'.format(token),
        }
        self.__issues_url__ = self.__ISSUES_URL__.format(username)

    def get_task_issues(self):
        issues = requests.get(
            self.__issues_url__ + '?state=open&creator={}'.format(self.__username__), self.__headers__).json()
        # Drop pull requests. https://developer.github.com/v3/issues/#list-issues-for-a-repository
        issues = list(filter(lambda i: 'pull_request' not in i, issues))
        # Find [Task] issue
        issues = list(filter(lambda i: re.match(self.__ISSUE_TITLE_REGEX__, i['title']), issues))
        return issues

    def get_task_issue_question_numbers(self):
        issues = self.get_task_issues()
        question_numbers = list(map(lambda i: int(re.search(self.__ISSUE_TITLE_REGEX__, i['title']).group(1)), issues))
        return question_numbers

    def create_task_issue(self, number):
        questions = LocalResource.get_questions()
        q = next(q for q in questions if q['number'] == number)
        title = self.__ISSUE_TITLE__.format(number, q['name'])
        req = requests.post(self.__issues_url__, headers=self.__headers__, json={
            'title': title,
            'body': self.__ISSUE_BODY__.format(q['url']),
            'labels': [q['difficulty']],
            'assignees': [self.__username__],
        })
        if req.status_code == 201:
            print('[INFO] Issue created: {} - {}'.format(title, q['url']))
        else:
            print('[ERROR] Failed to create issue. HTTP {}: {}'.format(req.status_code, req.json()['message']))

        return req.json()
