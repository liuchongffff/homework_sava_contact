from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_pageobject.pages.add_member_page import AddMemberPage
from test_pageobject.pages.basepage import BasePage
from test_pageobject.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _contanc_pos = (By.ID, "menu_contacts")
    def go_to_contact(self):
        self.find(*self._contanc_pos).click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.find(By.CSS_SELECTOR,"[node-type='addmember']").click()
        return AddMemberPage(self.driver)

if __name__ == '__main__':
    main = MainPage()
    main.go_to_add_member().add_member().save_member()