import os
from constant import Constant
from local import LocalResource


class Generator:
    @staticmethod
    def generate():
        index = '## Solutions\n'

        for q in LocalResource.get_solved_questions():
            index = index + '[#{}: {}](solutions/{})\n'.format(q['number'], q['name'], q['number'])
            content = '# Question {}: {}\n'.format(q['number'], q['name'])
            content = content + '[Link]({})\n\n'.format(q['url'])
            content = content + '## Solution\n'
            with open(os.path.join(Constant.SOLUTIONS_PATH, '{}/solution.md'.format(q['number'])), 'r') as f:
                content = content + f.read()
            content = content + '\n## Code\n'

            for file_name in os.listdir(Constant.SOLUTIONS_PATH + str(q['number'])):
                if file_name == 'code.java':
                    content = content + '#### Java\n'
                    content = content + '```java\n'
                    with open(os.path.join(Constant.SOLUTIONS_PATH, '{}/{}'.format(q['number'], file_name)), 'r') as f:
                        content = content + f.read()
                    content = content + '```\n'

            generated_file_name = Constant.BUILD_PATH + 'solutions/{}.md'.format(q['number'])
            os.makedirs(os.path.dirname(generated_file_name), exist_ok=True)
            with open(generated_file_name, 'w+') as f:
                f.write(content)

        with open(Constant.BUILD_PATH + 'index.md', 'w+') as f:
            f.write(index)
