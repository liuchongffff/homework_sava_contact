from time import sleep

from test_selenium_case.Base import Base


class TestMultiWindow(Base):

    def test_multiwindow_func(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()

        print(self.driver.current_window_handle)

        self.driver.find_element_by_link_text("立即注册").click()

        print(self.driver.current_window_handle)
        print(self.driver.window_handles)

        windows = self.driver.window_handles

        #self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("15021555147")
        sleep(5)

        #self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("15021555147")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(27)

