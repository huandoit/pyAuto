#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/15 11:18
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : base_driver.py
@Software: PyCharm
@description: 初始化浏览器
"""


from selenium import webdriver


class BaseDriver(object):

    def __init__(self):
        self.driver = webdriver.Chrome()


if __name__ == '__main__':
    driver = BaseDriver().driver
    print(driver)
