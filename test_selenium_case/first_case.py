import selenium
from selenium import webdriver


def test_selnium():
    test_driver_ins = webdriver.Chrome()
    test_driver_ins.get("https://www.baidu.com/")