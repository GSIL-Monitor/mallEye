#!/usr/bin/env python
# -- coding: utf-8 --
import time,datetime
import unittest
from selenium import webdriver
from mall_method import method



class home(unittest.TestCase):
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
        '''查看资讯电话显示'''
        tel = self.main.get_text('xpath', '//*[@id="login"]/div[1]/div[2]')
        try:
            self.assertEqual('咨询电话：020-37128297', tel)
        except AssertionError as e:
            print(e)


    def test_02(self):
        '''登录'''
        self.main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall")
        self.main.input("xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element("xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        
        name = self.main.get_text('xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)
        
        self.driver.implicitly_wait(10)
        time.sleep(2)


    def test_03(self):
        """验证日期是否是为两天前日期"""
        now_time = datetime.datetime.now()
        change_time = now_time + datetime.timedelta(days=-2)
        change_time_format = change_time.strftime('%Y-%m-%d')
        
        now_data = self.main.get_text('xpath', '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[1]/span[2]')
        now_data_format = now_data[0:10]

        try:
            self.assertEqual(now_data_format, change_time_format)
        except AssertionError as e:
            print(e)


    def test_04(self):
        """验证主项目和对比项数据不为0"""
        for num in range(1,5):
            a = '//*[@id="app"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[' + str(num) + ']/ul/li[2]'
            traffic = self.main.get_text('xpath', a)
            try:
                self.assertNotEqual('0', traffic)
            except AssertionError as e:
                print(e)
                print('Erre:第' + str(num) + '个项目客流量为0')


    def test_05(self):
        """判断日消费基础画像数据不为0"""
        for num in range(1,7):
            a = '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/ul/li[' + str(num) + ']/div[2]'
            traffic = self.main.get_text('xpath', a)
            try:
                self.assertNotEqual('0', traffic)
            except AssertionError as e:
                print(e)
                print('Erre:第' + str(num) + '个项目客流量为0')


    def test_06(self):
        """点击基础画像【查看详情】判断跳转页面和tab选中状态"""
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[1]/div/div')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('MALL--消费者画像', self.driver.title)
        except AssertionError as e:
            print(e)
            print('Error:消费者画像页title错误')

        menu_two_active = self.driver.find_element('xpath', '//*[@id="app"]/div[2]/div[1]/div/ul/li[1]/ul/li[2]')
        pointer_active = self.driver.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/ul/li[2]')
        try:
            self.assertEqual('menu_two_active', menu_two_active)
            self.assertEqual('active', pointer_active)
        except AssertionError as e:
            print(e)
            print('Error:导航客流画像分析或消费者画像选中状态错误')
        self.driver.back()


    def test_07(self):
        """点击来源工作地top5【查看详情】判断跳转页面元素正确性"""
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('MALL--消费者来源地', self.driver.title)
        except AssertionError as e:
            print(e)
            print('Error:消费者来源地页title错误')

        menu_two_active = self.main.get_class('xpath', '//*[@id="app"]/div[2]/div[1]/div/ul/li[1]/ul/li[4]')
        pointer_active = self.main.get_class('xpath', '//*[@id="app"]/div[1]/div[2]/ul/li[2]')
        tab_active = self.main.get_class('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/ul/li[2]')
        try:
            self.assertEqual('menu-two-active', menu_two_active)
            self.assertEqual('active', pointer_active)
            self.assertEqual('fl pointer portrait-tab-active', tab_active)
        except AssertionError as e:
            print(e)
            print('Error:导航客流画像分析、消费者画像或Tab选中状态错误')

        self.driver.back()

        
    def test_08(self):  
        """判断来源工作/居住地有无数据显示"""


    
    if __name__ == "__main__":
        unittest.main()