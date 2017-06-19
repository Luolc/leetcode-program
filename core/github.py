import requests
import json
from constant import Constant


class GitHubClient:
    BASE_URL = 'https://api.github.com/'

    ISSUES_URL = BASE_URL + 'repos/{}/leetcode-program/issues'

    ISSUE_TITLE = 'NO.{}: {}'

    ISSUE_BODY = 'Question link: {}'

    def __init__(self, username, token=''):
        self.__username__ = username
        self.__token__ = token
        self.__headers__ = {
            'User-Agent': username,
            'Authorization': 'token {}'.format(token),
        }
        self.__issues_url__ = self.ISSUES_URL.format(username)

    def get_task_issues(self):
        issues = requests.get(
            self.__issues_url__ + '?state=open&creator={}'.format(self.__username__), self.__headers__).json()
        issues = list(filter(lambda x: 'pull_request' not in x, issues))
        return issues

    def create_task_issue(self, number):
        with open(Constant.QUESTIONS_PATH, 'r') as f:
            questions = json.load(f)
        q = next(q for q in questions if q['number'] == number)
        title = self.ISSUE_TITLE.format(number, q['name'])
        req = requests.post(self.__issues_url__, headers=self.__headers__, json={
            'title': title,
            'body': self.ISSUE_BODY.format(q['url']),
            'labels': [q['difficulty']],
            'assignees': [self.__username__],
        })
        if req.status_code == 201:
            print('[INFO] Issue created: {} - {}'.format(title, q['url']))
        else:
            print('[ERROR] Failed to create issue. HTTP {}: {}'.format(req.status_code, req.json()['message']))

print(GitHubClient('Luolc').get_task_issues())
# GitHubClient('Luolc', 'de5aef24970883c21b6501e8754ac5ba551dcec6').create_task_issue(2)
