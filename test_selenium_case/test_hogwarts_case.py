from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_hogwarts_func(self):
        tttt = self.driver.find_element(By.CSS_SELECTOR, "#kw")
        print(tttt)
        tttt.send_keys("霍尔沃兹测试学院")

        sleep(30)
        submit_key = self.driver.find_element(By.ID,"su")
        print(submit_key)
        submit_key.click()
        sleep(7)
