#!/usr/bin/env python
# -- coding: utf-8 --
import unittest
from selenium import webdriver
from mall_method import method


class login(unittest.TestCase):
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
        '''查看登录页资讯电话显示'''
        tel = self.main.get_text('xpath', '//*[@id="login"]/div[1]/div[2]')
        try:
            self.assertEqual('咨询电话：020-37128297', tel)
        except AssertionError as e:
            print(e)

    def test_02(self):
        '''用户名登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        name = self.main.get_text(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)

    def test_03(self):
        '''退出登录'''
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[3]')
        self.main.click_element(
            'xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('MALL眼--数据报告', self.driver.title)
        except AssertionError as e:
            print(e)
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[3]')
        self.main.click_element(
            'xpath', '/html/body/div[2]/div/div[3]/button[2]')

    def test_04(self):
        '''邮箱登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "317888988@qq.com")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        name = self.main.get_text(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[3]')
        self.main.click_element(
            'xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.driver.implicitly_wait(10)

    def test_05(self):
        '''手机号登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "14700000000")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        name = self.main.get_text(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[3]')
        self.main.click_element(
            'xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.driver.implicitly_wait(10)

    def test_06(self):
        '''昵称登录'''
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[2]/div/input", "wsmall_679732130")
        self.main.input(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[3]/div/input", "ws2018")
        self.main.click_element(
            "xpath", "//*[@id='login']/div[2]/div[2]/div[4]")
        name = self.main.get_text(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[2]')
        self.driver.implicitly_wait(10)
        try:
            self.assertEqual('wsmall_679732130', name)
        except AssertionError as e:
            print(e)
        self.main.click_element(
            'xpath', '//*[@id="app"]/div[1]/div[3]/span[3]')
        self.main.click_element(
            'xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.driver.implicitly_wait(10)
