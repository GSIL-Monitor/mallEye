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

    def test(self):
        '''登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        self.driver.implicitly_wait(10)

    def test_01(self):
        '''进入客流画像分析->客流趋势分析页'''
        self.main.get_content_click('xpath', '客流画像分析')
        self.driver.implicitly_wait(10)

    def test_02(self):
        '''验证基础画像显示加载成功'''
        flowechars = self.main.get_class('id', 'flowechars')
        print(flowechars)
        try:
            self.driver.find_element(
                'xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/div[3]')
        except:
            print('加载失败')

if __name__ == "__main__":
    unittest.main()
