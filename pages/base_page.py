#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/15 11:16
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : base_page.py
@Software: PyCharm
@description: 页面基础类
"""

import time
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self):
        self.driver = BaseDriver().driver
        self.url = 'http://172.18.1.187/#/login'

    def open(self, url):
        """ 访问网址 """
        self.driver.get(url)

    def find_element(self, *selector):
        """ 重写查找单个元素 """
        return self.driver.find_element(*selector)

    def find_elements(self, *selector):
        """ 重写查找多个元素 """
        return self.driver.find_elements(*selector)

    def login(self, username, password):
        """ 统一登录 """
        input_username = (By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[2]/div/input')
        input_password = (By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[3]/div/input')
        submit_btn = (By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[4]/button')
        self.open(self.url)
        self.find_element(*input_username).send_keys(username)
        self.find_element(*input_password).send_keys(password)
        self.find_element(*submit_btn).click()
        time.sleep(5)


if __name__ == '__main__':
    base_page = BasePage()
    base_page.login('root', '111111')
