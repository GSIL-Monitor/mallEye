# -- coding: utf-8 --
import time
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
        time.sleep(1)
        self.main.get_content_click('xpath', '客流画像分析')
        self.main.get_content_click('xpath', '消费者画像')
        time.sleep(2)
        
    def test_01(self):
        '''消费者画像-基础画像：显示所有基础画像'''
        arr = ['chartsIdSex', 'chartsIdAge', 'chartsIdJod', 'chartsIdEducation']
        for num in range(len(arr)):
            a = '//*[@id="' + arr[num] + '"]/div[1]/canvas'
            self.assertIsNotNone(a, '画像加载失败')

    def test_02(self):
        '''切换经济画像：显示所有画像'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/ul/li[2]')
        time.sleep(2)
        arr = ['chartsIdMoney', 'chartsIdHome', 'chartsIdTraffic']
        for num in range(len(arr)):
            a = '//*[@id="' + arr[num] + '"]/div[1]/canvas'
            self.assertIsNotNone(a, '画像加载失败')

    def test_03(self):
        '''切换偏好画像：显示所有画像'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[2]/ul/li[3]')
        time.sleep(2)
        arr = ['chartsIdTravel', 'chartsIdFood']
        for num in range(len(arr)):
            a = '//*[@id="' + arr[num] + '"]/div[1]/canvas'
            self.assertIsNotNone(a, '画像加载失败')
        self.assertIsNotNone('//*[@id="app"]/div[2]/div[2]/div/div[2]/div[3]/div[5]/div[2]/div[1]/div/div[2]/ul/li[2]/div', '画像加载失败')

    def test_04(self):
        '''切换到访分析TAB页：显示新老顾客和平均到访频次画像'''
        self.main.get_content_click('xpath', '到访分析')
        time.sleep(2)
        self.assertIsNotNone('//*[@id="chartVisit"]/div[1]/canvas', '平均到访频次画像加载失败')
        self.assertIsNotNone('//*[@id="chartCustomer1"]/div[1]/canvas', '新老顾客画像加载失败')


if __name__ == "__main__":
    unittest.main()