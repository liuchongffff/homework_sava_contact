from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestHogwarts():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_hogwarts_func(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        action_ins = ActionChains(self.driver)

        elment_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        elment_double_click = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        element_right_click = self.driver.find_element_by_xpath('/html/body/form/input[4]')

        action_ins.click(elment_click)
        action_ins.double_click(elment_double_click)
        action_ins.context_click(element_right_click)
        action_ins.perform()
        sleep(10)
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        #ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action_ins = ActionChains(self.driver)

        action_ins.move_to_element(ele)

        action_ins.perform()
        sleep(10)


    @pytest.mark.skip
    def test_dragdrop_ele(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        #ele = self.driver.find_element_by_link_text("设置")
        ele_1 = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        ele_2 = self.driver.find_element_by_xpath('/html/body/div[2]')
        action_ins = ActionChains(self.driver)

        action_ins.drag_and_drop(ele_1,ele_2)

        action_ins.perform()
        sleep(10)

    @pytest.mark.skip
    def test_simulate_key(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele_1.click()
        action_ins = ActionChains(self.driver)
        action_ins.send_keys("username").pause(2)
        action_ins.send_keys(Keys.SPACE).pause(2)
        action_ins.send_keys("tom").pause(2)
        action_ins.send_keys(Keys.BACK_SPACE).perform()
        sleep(10)

    def test_touchaction(self):
        self.driver.get("https://www.baidu.com/")
        el_1 = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")

        el_1.send_keys("selenium 测试")
        action_ins = TouchActions(self.driver)
        action_ins.tap(el_search)
        sleep(10)

        action_ins.scroll_from_element(el_1,0,10000).perform()
        sleep(10)

