#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/16 10:23
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : login.py
@Software: PyCharm
@description: 登录页面代码，没有进行PO划分，包含所有内容
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self):
        """ 初始化浏览器 """
        self.driver = webdriver.Chrome()
        self.url = 'http://172.18.1.187/#/login'
        self.driver.get(self.url)

    def input_username(self, username):
        """ 输入用户名 """
        element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[2]/div/input')
        element.send_keys(username)

    def input_password(self, password):
        """ 输入密码 """
        element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[3]/div/input')
        element.send_keys(password)

    def clcik_submit(self):
        element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[4]/button')
        element.click()


if __name__ == '__main__':
    login = Login()
    login.input_username('root')
    login.input_password('111111')
    login.clcik_submit()