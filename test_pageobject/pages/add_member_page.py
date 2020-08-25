from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_pageobject.pages.basepage import BasePage
from test_pageobject.pages.contact_page import ContactPage


class AddMemberPage (BasePage):
    _user_name_pos = (By.ID,"username")
    _acctid_pos = (By.ID, "memberAdd_acctid")
    _phone_num_pos = (By.ID, "memberAdd_phone")
    _cancle_save_pos = (By.CSS_SELECTOR, ".js_btn_cancel")
    _cancle_pos = (By.CSS_SELECTOR,"[node-type='cancel']")
    def add_member(self,user_name = None, acc_id= None,phone_num = None):
        self.find(*self._user_name_pos).send_keys(user_name)
        self.find(*self._acctid_pos).send_keys(acc_id)
        self.find(*self._phone_num_pos).send_keys(phone_num)
        return self

    def save_member(self):
        self.wait_for_clickable((By.CSS_SELECTOR,".js_btn_save"))
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return ContactPage(self.driver)


    def cancel_member(self):
        self.find(*self._cancle_save_pos).click()
        self.wait_for_clickable(self._cancle_pos)
        self.find(*self._cancle_pos).click()
        return ContactPage(self.driver)