from time import sleep

from selenium.webdriver.common.by import By

from test_pageobject.pages.basepage import BasePage



class AddDepartmentPage (BasePage):
    _add_new_depart_pos =  (By.CSS_SELECTOR, ".ww_inputText:nth-child(2)")
    _select_drop_pos = (By.CSS_SELECTOR, "#__dialog__MNDialog__ .ww_btn_Dropdown")

    #_select_owned_depart_pos = (By.XPATH, "//a[contains(text(), '上海电气数字科技')][2]")
    _select_owned_depart_pos = (By.XPATH, "//a[@id=\"1688850914903345_anchor\"]")
    save_button_pos = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck=\"submit\"]")
    cancel_button_pos = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck=\"cancel\"]")

    def add_new_department(self, dpart_name):
        self.find(*self._add_new_depart_pos).send_keys(dpart_name)
        self.find(*self._select_drop_pos).click()
        sleep(3)
        elem_list = self.finds(*self._select_owned_depart_pos)
        if elem_list is not None:
            elem_list[1].click()
        sleep(2)
        return self

    def save_new_department(self):
        from test_pageobject.pages.contact_page import ContactPage
        sleep(5)
        self.find(*self.save_button_pos).click()
        return ContactPage(self.driver)

    def cancel_new_department(self):
        from test_pageobject.pages.contact_page import ContactPage
        sleep(5)
        self.find(*self.cancel_button_pos).click()
        return ContactPage(self.driver)

