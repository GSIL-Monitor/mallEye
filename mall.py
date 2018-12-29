#!/usr/bin/env python
# -- coding: utf-8 --
from selenium.webdriver.support import expected_conditions as EC
from mall_method import method
from selenium import webdriver
import unittest
import time
import datetime


class winshang(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://eye.winshangdata.com"
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        # 登录
        main = method(self.driver)
        main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall")
        main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        main.click_element("xpath", "//*[@id='login']/div[2]/div[2]/div[4]")

        name = main.get_text('xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)
        
        self.driver.implicitly_wait(10)

        # 获取两天前的日期
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=-2)
        change_time_format = change_time.strftime('%Y-%m-%d')
        
        now_data = main.get_text('xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[1]/span[2]')
        now_data_format = now_data[0:10]

        try:
            self.assertEqual(now_data_format, change_time_format)
        except AssertionError as e:
            print(e)

    def test_report_day(self):
        # 日/周/月报
        # 获取当前时间
        # date = time.strftime("%Y-%m-%d", time.localtime())

        
        main = method(self.driver)
        main.click_element('xpath', '//*[@id="app"]/div[2]/div[1]/div[1]/div/div[2]/div/span')
        
        self.driver.implicitly_wait(10)
        




if __name__ == "__main__":
    unittest.main()
