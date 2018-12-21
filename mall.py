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
        main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "nini317")
        main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "12345678")
        main.click_element("xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        self.driver.implicitly_wait(10)

        main.assertEql('xpath', '//*[@id="app"]/div[1]/div[3]/span[2]', 'Hi!   test011')

    def test_report_day(self):
        # 日/周/月报
        # 获取当前时间
        # date = time.strftime("%Y-%m-%d", time.localtime())

        # 两天前的日期
        '''
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=-2)
        change_time_format = change_time.strftime('%Y-%m-%d')
        print(change_time_format)
        '''
        main = method(self.driver)
        main.click_element('xpath', '//*[@id="app"]/div[1]/div[2]/ul/li[2]/span')
        self.driver.implicitly_wait(10)
        time.sleep(3)




if __name__ == "__main__":
    unittest.main()
