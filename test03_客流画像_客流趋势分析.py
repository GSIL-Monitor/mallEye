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
        
    def test_01(self):
        '''进入客流趋势分析页：显示趋势图画像'''
        self.main.get_content_click('xpath', '客流画像分析')
        self.driver.implicitly_wait(10)
        flowechars = self.main.get_class('id', 'flowechars')
        self.assertEqual('mall-chart', flowechars)

    def test_02(self):
        '''切换客群：显示验证趋势图'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div')
        # self.main.click_element('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
        flowechars = self.main.get_class('id', 'flowechars')
        self.assertEqual('mall-chart', flowechars)

    def test_03(self):
        '''切换时间段【近30天】:显示趋势图和按周可点击'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/label[2]')
        flowechars = self.main.get_class('id', 'flowechars')
        self.assertEqual('mall-chart', flowechars)
        week = self.main.get_class('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[5]/label[2]')
        self.assertEqual('el-radio-button el-radio-button--mini', week)

    def test_04(self):
        '''切换时间段【前天】:显示趋势图加载和按日/时可点击'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/label[3]')
        flowechars = self.main.get_class('id', 'flowechars')
        self.assertEqual('mall-chart', flowechars)
        time_day = self.main.get_class('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[5]/label[4]')
        self.assertEqual('el-radio-button el-radio-button--mini is-active', time_day)
        time_hours = self.main.get_class('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[5]/label[1]')
        self.assertEqual('el-radio-button el-radio-button--mini', time_hours)

    def test_05(self):
        '''开启对比时间段：显示趋势图'''
        self.main.click_element('xpath', '//*[@id="app"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/span[2]/label/span[1]')
        flowechars = self.main.get_class('id', 'flowechars')
        self.assertEqual('mall-chart', flowechars)


if __name__ == "__main__":
    unittest.main()