from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
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

        def wait_func(x):
            return len(self.driver.find_elements(By.XPATH, '// * [ @ id = "hot_teams"] /  div[2] / div / div[1] / div / div[2] / div[1] / a')) >= 1

        WebDriverWait(self.driver, 10 ).until(wait_func)

        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-23386 .title > a").click()
        sleep(5)
