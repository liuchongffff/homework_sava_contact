from time import sleep

from selenium.webdriver.common.by import By

from test_pageobject.pages.add_department_page import AddDepartmentPage
from test_pageobject.pages.basepage import BasePage


class ContactPage(BasePage):
    _add_member_pos = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member:nth-child(2)")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")

    _add_pos = (By.CSS_SELECTOR, "#main .member_colLeft_top_addBtn")
    _add_depart_pos = (By.CSS_SELECTOR, "#main .js_create_party")

    _display_jstree1 = (By.CSS_SELECTOR, ".jstree-anchor")

    def go_to_add_member(self):
        from test_pageobject.pages.add_member_page import AddMemberPage

        self.wait_for_clickable(self._add_member_pos)

        while True:
            self.find(*self._add_member_pos).click()
            # 报错被捕获，执行except循环点击找元素操作，直到找到为主
            try:
                # 找到添加成员页面的某个元素
                res = self.find(*self._cancel)
                # 如果存在的话就跳出循环，如果不存在的话，就报错
                if res is not None:
                    print("已经找到")
                    print(res)
                    break
            except:
                print("暂时没找到")

        return AddMemberPage(self.driver)

    def go_to_add_department(self):
        self.find(*self._add_pos).click()
        sleep(3)
        self.find(*self._add_depart_pos).click()
        return AddDepartmentPage(self.driver)

    def get_member_list(self):
        sleep(5)
        ele_list_ins = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(ele_list_ins)
        for name in ele_list_ins:
            print(name.text)
        return [tst_name.text for tst_name in ele_list_ins]

    def get_depart_list(self):
        sleep(5)
        ele_list_ins = self.finds(*self._display_jstree1)
        return [tst_name.text for tst_name in ele_list_ins]
