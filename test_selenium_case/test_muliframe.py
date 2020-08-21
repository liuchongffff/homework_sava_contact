from time import sleep

from test_selenium_case.Base import Base


class TestMultiFrame(Base):

    def test_multiframe_func(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)

        self.driver.switch_to.default_content()

        print(self.driver.find_element_by_id("submitBTN").text)
