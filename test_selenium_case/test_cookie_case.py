import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookieCase():
    def setup(self):
        # option_ins = webdriver.ChromeOptions()
        # option_ins.debugger_address = '127.0.0.1:9222'

        # self.driver = webdriver.Chrome(options=option_ins)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_cookie_func(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'g-o4JB5gTzPnf5I9I4fOgWKq5I9PP5WMLIKSpS57c_mH-JciJgxMaUFw6_DBWpRQSV4KW1606VD5ip-1NsVqJL3Nd0vN2JWUfU99UuC62QQHvYWA_t_LCGKsrAIVe3SFzSAC6Ea_6c-DGNc8XqzOlqiCS8ndTpoq35RjyZgRPPuwn8biA4WJ78j7pJ9OCZ63Pu1DHOa1TSs724tPWuQndUR0_ShCNKkFywaTxfG05zxs_PQWV7ZOgYDayTliFMe_zJJAuRw0-1X5aXI2McCaHw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'KneP0boeL4-zSxgYi3ooP43pWzBX3n5GQypS4pmOzr0yUXY3fzHpJkHEyihrsonX'},
            {'domain': '.qq.com', 'expiry': 1598066274, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.413607970.1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2594368512'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598010720, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '16d61o2'},
            {'domain': '.qq.com', 'expiry': 1661051874, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.720220497.1597235624'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '0b11ceb8e01606708d2777154e1907a61ad24a8c65a0046600bf75857f0adb12'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771620, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600571877, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6114686'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629515185, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1597235622,1597652201,1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1567376094384124'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'VRxUVjacb7'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324955153827'},
            {'domain': '.qq.com', 'expiry': 1877496553, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5d1c4fe97cbd7'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6483960718'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        cookies_ins_2 = self.driver.get_cookies()
        print(cookies_ins_2)
        sleep(20)

    @pytest.mark.skip
    def test_import_contact_func(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597993791'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'vGLusT2luOlMqYh67nFbKSAzI6ooGqOG4a-QVvGebtDIxuIKXs6n7hI49QCNgVnhom7rU_yzkNLUQj_9xHXFi5L_tiYP3vsjIYYFHXHdPnQk_UqQTul37QQ6j6SpF3Cn8ahYbhY-IowFjYbWbkcU5eK0KrT16mEuFJH8YqpRj2hyoOOaEZ6YI3NQN-sn8UXQkHfVtSMeID45masDoyPI1FrqFxqhqQ4aTRLfWswyX5tW0JySJiOIF1ACF8TrpLceptzX9cFq5M5Z2I0sWKw8NA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'KneP0boeL4-zSxgYi3ooP1QW4FRM49e3K3I2YjiB_DYh9v8hbu0X1E_jh9cduAQB'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1598080195, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.413607970.1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2594368512'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598010720, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '16d61o2'},
            {'domain': '.qq.com', 'expiry': 1661065795, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.720220497.1597235624'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '0b11ceb8e01606708d2777154e1907a61ad24a8c65a0046600bf75857f0adb12'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771620, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600585798, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6245991'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629529791, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1597235622,1597652201,1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1567376094384124'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'VRxUVjacb7'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324955153827'},
            {'domain': '.qq.com', 'expiry': 1877496553, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5d1c4fe97cbd7'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6483960718'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_file_input").send_keys(
            "E:\share\project\python_selenium\\test_selenium_case\mydata.xlsx")
        assert "mydata.xlsx" == self.driver.find_element(By.CSS_SELECTOR, "#upload_file_name").text
        sleep(30)

    @pytest.mark.skip
    def test_shelves_case(self):
        #shelve python内置的模块，相当于小型的数据库
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597993791'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'vGLusT2luOlMqYh67nFbKSAzI6ooGqOG4a-QVvGebtDIxuIKXs6n7hI49QCNgVnhom7rU_yzkNLUQj_9xHXFi5L_tiYP3vsjIYYFHXHdPnQk_UqQTul37QQ6j6SpF3Cn8ahYbhY-IowFjYbWbkcU5eK0KrT16mEuFJH8YqpRj2hyoOOaEZ6YI3NQN-sn8UXQkHfVtSMeID45masDoyPI1FrqFxqhqQ4aTRLfWswyX5tW0JySJiOIF1ACF8TrpLceptzX9cFq5M5Z2I0sWKw8NA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'KneP0boeL4-zSxgYi3ooP1QW4FRM49e3K3I2YjiB_DYh9v8hbu0X1E_jh9cduAQB'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1598080195, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.413607970.1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2594368512'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598010720, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '16d61o2'},
            {'domain': '.qq.com', 'expiry': 1661065795, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.720220497.1597235624'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850132002621'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '0b11ceb8e01606708d2777154e1907a61ad24a8c65a0046600bf75857f0adb12'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771620, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600585798, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6245991'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629529791, 'httpOnly': False,
                                    'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                    'value': '1597235622,1597652201,1597979186'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '1567376094384124'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'VRxUVjacb7'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324955153827'},
            {'domain': '.qq.com', 'expiry': 1877496553, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '0_5d1c4fe97cbd7'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '6483960718'}]

        db = shelve.open('./mydbs/cookies')
        db['cookie'] = cookies
        db.close()

    def test_shelves_case_2(self):
        #shelve python内置的模块，相当于小型的数据库
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_file_input").send_keys(
            "E:\share\project\python_selenium\\test_selenium_case\mydata.xlsx")

        assert "mydata.xlsx" == self.driver.find_element(By.CSS_SELECTOR, "#upload_file_name").text
        #点击提交按钮
        self.driver.find_element(By.CSS_SELECTOR, "#submit_csv").click()
        #点击查看通讯录按钮
        self.driver.find_element(By.CSS_SELECTOR, "#reloadContact").click()
        #点击首页，回到首页
        self.driver.find_element(By.CSS_SELECTOR,"#menu_index").click()
        sleep(300)
