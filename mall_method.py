#!/usr/bin/env python
# -- coding: utf-8 --
import unittest

u'''
    1	assertEqual(a, b)	判断ab是否相等
    2	assertNotEqual(a, b)	判断ab不相等
    3	assertIs(a, b)　	判断a是b
    4	assertIsNot(a, b)	判断a不是b
    5	assertIsNone(a)	判断a是不是None
    6	assertIsNotNone(a)	判断a不是None
    7	assertIn(a,b)	判断a在b中，此时a与b可以相等
    8	assertNotIn(a, b)	判断a不在b中
    9	assertIsInstance(a, b)	判断a是否属于b的实例
    10	assertNotIsInstance(a, b)	判断a不属于b的实例 
    11	assertGreater(a, b)	判断a > b
    12	assertGreaterEqual(a, b)	判断a >= b 
    13	assertLess(a, b)	判断a < b 
    14	assertLessEqual(a, b)	判断a <= b 
'''

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

    # 判断内容是否存在相等
    def assertEql(self, type, loction, value):
        content = self.dr.find_element(type, loction).text
        print(content)
        self.assertEqual(value, content)