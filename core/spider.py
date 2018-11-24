from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException


class Spider:
    __URL__ = 'https://leetcode.com/problemset/algorithms/'

    def __init__(self, js_path='plantomjs'):
        self.__js_path__ = js_path

    def fetch_questions(self):
        driver = webdriver.PhantomJS(self.__js_path__)

        # Wait until the page is loaded
        print('[INFO] Waiting for page to be fully loaded...')
        wait = ui.WebDriverWait(driver, 10)
        driver.get(self.__URL__)
        wait.until(lambda d: d.find_element_by_xpath(r"//span[@class='row-selector']"))

        # Show all the problems
        driver.find_element_by_xpath(
            r"//span[@class='row-selector']/select[@class='form-control']").send_keys('all')
        print('[INFO] Loaded. Show all the problems.')

        questions = []
        tr_elements = driver.find_elements_by_xpath(
            r"//table[@class='table table-striped']//tbody[@class='reactable-data']//tr")
        question_amount = len(tr_elements)
        print('[INFO] Total: {} problems'.format(question_amount))

        for q in tr_elements:
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
            print('[INFO] Problem {} fetched.'.format(number))

        print('[INFO] Fetching completed. %d problems have been fetched.' % question_amount)
        return questions
