from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWaits():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("http://www.testerhome.com")
        self.driver.find_element_by_link_text("社团").click()


        WebDriverWait(self.driver, 10 ).until(expected_conditions.element_to_be_clickable((By.XPATH, '// * [ @ id = "hot_teams"] /  div[2] / div / div[1] / div / div[2] / div[1] / a')))

        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-23386 .title > a").click()
        sleep(5)
