from time import sleep

from test_selenium_case.Base import Base


class TestChromeCase(Base):
    def test_chrome_option_func(self):
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(35)
