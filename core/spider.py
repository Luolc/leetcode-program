from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Spider:
    __URL__ = 'https://leetcode.com/problemset/algorithms/'

    def __init__(self, js_path='plantomjs'):
        self.__js_path__ = js_path

    def fetch_questions(self):
        driver = webdriver.PhantomJS(self.__js_path__)
        driver.get(self.__URL__)
        # Show all the problems
        driver.find_element_by_xpath(r"//span[@class='row-selector']/select[@class='form-control']").send_keys('all')
        questions = []
        question_amount = 0
        for q in driver.find_elements_by_xpath(
                r"//table[@class='table table-striped']//tbody[@class='reactable-data']//tr"):
            locked = True
            try:
                q.find_element_by_xpath(r"td[3]//i")
            except NoSuchElementException:
                locked = False
            # Ignore the locked questions since we are poor. :-(
            if locked:
                continue

            number = q.find_element_by_xpath(r"td[2]").text
            url = q.find_element_by_xpath(r"td[3]//a").get_attribute('href')
            name = q.find_element_by_xpath(r"td[3]//a").text
            difficulty = q.find_element_by_xpath(r"td[6]").text
            questions.append({
                'number': int(number),
                'url': url,
                'name': name,
                'difficulty': difficulty
            })
            question_amount += 1
        print('[INFO] Fetching completed. %d problems have been fetched.' % question_amount)
        return questions
