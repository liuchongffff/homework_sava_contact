
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base():
    def setup(self):
        option_ins = webdriver.ChromeOptions()
        option_ins.debugger_address = '127.0.0.1:9222'

        self.driver = webdriver.Chrome(options=option_ins)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
