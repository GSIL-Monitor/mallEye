# -- coding: utf-8 --
import time
import datetime
import unittest
from selenium import webdriver
from mall_method import method


class test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.url = "http://eye.winshangdata.com"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.main = method(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_01(self):
        '''邮箱登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        time.sleep(2)
        # self.driver.find_element('xpath','//span[contains(text(),"客流画像分析")]').click()
        self.main.get_content_click('xpath', '客流画像分析')
        time.sleep(2)

        display = self.driver.find_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div[3]')
        assert display.is_displayed()

if __name__ == "__main__":
    unittest.main()
