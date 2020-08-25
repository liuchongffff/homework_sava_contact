import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_pageobject.pages.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize(
        "name, acc_id, phone", [("皮城女皇","3333","13388881234")]
    )
    def test_add_member(self,name,acc_id,phone):
        self.main = MainPage()
        # 1.从首页跳转到添加成员页面 2.添加成员
        name_list = self.main.go_to_add_member().add_member(name,acc_id,phone).save_member().get_member_list()
        assert "皮城女皇" in name_list

    @pytest.mark.parametrize(
        "name, acc_id, phone", [("皮城女皇2","3333","13388881234")]
    )
    def test_add_member_fail(self,name,acc_id,phone):
        self.main = MainPage()
        # 1.从首页跳转到添加成员页面 2.添加成员
        name_list = self.main.go_to_add_member().add_member(name,acc_id,phone).cancel_member().get_member_list()
        assert "皮城女皇2" not in name_list

    @pytest.mark.parametrize(
        "name, acc_id, phone", [("皮城女皇3","4444","13388881235")]
    )
    def test_contact_member(self,name,acc_id,phone):
        self.main = MainPage()
        # 1.从首页跳转到通讯录页面 2.跳转到添加成员 3.添加成员
        name_list = self.main.go_to_contact().go_to_add_member().add_member(name,acc_id,phone).save_member().get_member_list()

        assert "皮城女皇3" in name_list

    def teardown(self):
        self.main.driver.quit()

