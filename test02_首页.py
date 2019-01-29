#!/usr/bin/env python
# -- coding: utf-8 --
import time
import datetime
import unittest
from selenium import webdriver
from mall_method import method


class WinShang(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.main = method(self.driver)
        self.url = self.main.eye_url()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test(self):
        '''登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", self.main.username())
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", self.main.password())
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        self.driver.implicitly_wait(10)

    def test_02(self):
        """日报：日期是否为两天前日期"""
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=-2)
        change_time_format = change_time.strftime('%Y-%m-%d')

        now_data = self.main.get_text(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[1]/span[2]')
        now_data_format = now_data[0:10]
        self.assertEqual(now_data_format, change_time_format)

    def test_03(self):
        """日报：主项目和对比项数据不为0"""
        for num in range(1, 5):
            a = '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[' + \
                str(num) + ']/ul/li[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0', traffic)

    def test_04(self):
        """日报：日消费基础画像数据不为0"""
        for num in range(1, 7):
            a = '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/ul/li[' + \
                str(num) + ']/div[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0.00%', traffic)

    def test_05(self):
        """日报：点击基础画像【查看详情】跳转页面和tab选中状态验证"""
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/div/div')
        self.driver.implicitly_wait(10)

        menu_two_active = self.main.get_class(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div/ul/li[1]/ul/li[2]')
        pointer_active = self.main.get_class(
            'xpath', '//*[@id="app"]/div[1]/div[2]/ul/li[2]')
        self.assertEqual('menu-two-active', menu_two_active)
        self.assertEqual('active', pointer_active)
        self.driver.back()

    def test_06(self):
        """日报：点击来源工作地top5【查看详情】跳转页面验证"""
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]')
        self.driver.implicitly_wait(10)

        menu_two_active = self.main.get_class(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div/ul/li[1]/ul/li[4]')
        pointer_active = self.main.get_class(
            'xpath', '//*[@id="app"]/div[1]/div[2]/ul/li[2]')
        self.assertEqual('menu-two-active', menu_two_active)
        self.assertEqual('active', pointer_active)
        self.driver.back()

    def test_07(self):
        """切换周报：主项目和对比项数据不为0"""
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div')
        self.driver.implicitly_wait(10)
        time.sleep(1)

        for num in range(1, 5):
            a = '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[' + \
                str(num) + ']/ul/li[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0', traffic)

    def test_08(self):
        """周报：主项目天气信息不为空"""
        weather = self.main.get_text(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/span[2]')
        weathers = ((','.join(weather)).split(',')[0])
        w = int(weathers)
        if w < 0 or w > 0 or w == 0:
            print('平均最高温度:' + str(weather))
        else:
            print('Error:天气温度显示错误')
            print(weather)

    def test_09(self):
        """周报：日消费基础画像数据不为0"""
        for num in range(1, 7):
            a = '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/ul/li[' + \
                str(num) + ']/div[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0.00%', traffic)

    def test_10(self):
        """切换月报：主项目和对比项数据不为0"""
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div')
        self.driver.implicitly_wait(10)

        for num in range(1, 5):
            a = '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[' + \
                str(num) + ']/ul/li[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0', traffic)

    def test_11(self):
        """月报：日消费基础画像数据不为0"""
        for num in range(1, 7):
            a = '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/ul/li[' + \
                str(num) + ']/div[2]'
            traffic = self.main.get_text('xpath', a)
            self.assertNotEqual('0.00%', traffic)

    def test_12(self):
        '''验证未来五天天气'''
        for num in range(1, 6):
            a = '//*[@id="app"]/div[2]/div[1]/div[5]/div/div/ul/li[' + \
                str(num) + ']/p[3]'
            weather = self.main.get_text('xpath', a)
            w = len(weather)
            if w > 3 and num == 1:
                print('今日天气显示正常:' + weather)
            elif w > 3:
                print('第' + str(num) + '天温度显示正常:' + weather)
            else:
                print('Error:天气显示错误')
                print(weather)
                
if __name__ == "__main__":
    unittest.main()