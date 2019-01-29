#!/usr/bin/env python
# -- coding: utf-8 --
import unittest
from selenium import webdriver


class method ():
    def __init__(self, driver):
        self.dr = driver
    # 公共信息
    def eye_url(self):
        url = "http://eye.winshangdata.com"
        return url

    def username(self):
        username = "wsmall"
        return username

    def password(self):
        password = "ws2018"
        return password
        

    # 点击元素
    def click_element(self, type, value):
        self.dr.find_element(type, value).click()

    # 输入内容
    def input(self, type, value1, value2):
        self.dr.find_element(type, value1).click()
        self.dr.find_element(type, value1).send_keys(value2)

    # 获取元素文本内容
    def get_text(self, type, value):
        return self.dr.find_element(type, value).text

    # 获取class
    def get_class(self, type, value):
        return self.dr.find_element(type, value).get_attribute("class")

    # 获取input Value值
    def get_inputValue(self, type, value):
        return self.dr.find_element(type, value).get_attribute("value")
    
    # 通过获取元素文本内容定位元素
    def get_content_click(self, type, value):
        content = '//span[contains(text(),"' + value + '")]'
        self.dr.find_element(type, content).click()

    def li_content_click(self, type, value):
        content = '//li[contains(text(),"' + value + '")]'
        self.dr.find_element(type, content).click()