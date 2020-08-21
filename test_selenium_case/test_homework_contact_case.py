"""
通过保存的cookie，登陆企业微信界面，然后导入事先保存在mydata.xlsx的文件【里面有两条数据】，增加断言确定导入成功
"""


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

    def test_shelves_savecontact_case(self):
        #shelve python内置的模块，相当于小型的数据库
        #获取保存在cookies数据库中cookies值
        db = shelve.open('./mydbs/cookies')
        cookies = db['cookie']

        #打开微信界面，为了后续输入cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #再加入cookie之后，再次打开
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #点击导入通讯录界面
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        #选择上传文件
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_file_input").send_keys(
            "E:\share\project\python_selenium\\test_selenium_case\mydata.xlsx")

        assert "mydata.xlsx" == self.driver.find_element(By.CSS_SELECTOR, "#upload_file_name").text
        #点击提交按钮
        self.driver.find_element(By.CSS_SELECTOR, "#submit_csv").click()

        #验证是否到了询问查看通讯录界面
        print(self.driver.find_element(By.CSS_SELECTOR, "#reloadContact").text)
        assert "前往查看" == self.driver.find_element(By.CSS_SELECTOR, "#reloadContact").text

        #点击查看通讯录按钮
        self.driver.find_element(By.CSS_SELECTOR, "#reloadContact").click()
        #点击首页，回到首页
        self.driver.find_element(By.CSS_SELECTOR,"#menu_index").click()
        sleep(20)
