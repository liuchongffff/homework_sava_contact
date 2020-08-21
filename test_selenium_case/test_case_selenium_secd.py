from time import sleep

from selenium import webdriver

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("http://www.testerhome.com")
        #sleep(1)
        self.driver.find_element_by_link_text("社团").click()
        #sleep(1)
        self.driver.find_element_by_link_text("求职面试圈").click()
        #sleep(1)
        self.driver.find_element_by_css_selector(".topic-23386 .title > a").click()
        #sleep(1)

        pass