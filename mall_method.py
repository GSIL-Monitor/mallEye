#!/usr/bin/env python
# -- coding: utf-8 --


class method ():
    def __init__(self, driver):
        self.dr = driver

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
