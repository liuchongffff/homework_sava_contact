import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_pageobject.pages.main_page import MainPage


class TestAddDepartment:
    def test_add_new_department(self):
        self.main = MainPage()
        # 1.从首页跳转到contact页面 2.添加新部门 #保存成功
        name_list = self.main.go_to_contact().go_to_add_department().add_new_department("软件创新中心").save_new_department().get_depart_list()
        assert "软件创新中心" in name_list

    def test_add_new_department_fail(self):
        self.main = MainPage()
        # 1.从首页跳转到contact页面 2.添加新部门 3.取消保存
        name_list = self.main.go_to_contact().go_to_add_department().add_new_department("互联网创新中心").cancel_new_department().get_depart_list()
        assert "互联网创新中心" not in name_list
