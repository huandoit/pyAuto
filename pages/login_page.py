#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/15 15:33
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : login_page.py
@Software: PyCharm
@description: 登录页面类
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """ 登录页面 """

    # def __init__(self):
    #     """ 初始化浏览器 """
    #     self.driver = webdriver.Chrome()
    #     self.url = 'http://172.18.1.187/#/login'
    #     self.driver.get(self.url)

    username_input = (By.XPATH, '//input[@placeholder="用户名"]')
    password_input = (By.XPATH, '//input[@placeholder="密码"]')
    submit_btn = (By.XPATH, '//button[@type="submit"]')

    def login_page(self, url):
        """ 进入登录页面 """
        self.open(url)

    def input_username(self, username):
        """ 输入用户名 """
        # element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[2]/div/input')
        # element.send_keys(username)
        self.find_element(*self.username_input).send_keys(username)

    def input_password(self, password):
        """ 输入密码 """
        # element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[3]/div/input')
        # element.send_keys(password)
        self.find_element(*self.password_input).send_keys(password)

    def clcik_submit(self):
        """ 点击登录按钮 """
        # element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[4]/button')
        # element.click()
        self.find_element(*self.submit_btn).click()


if __name__ == '__main__':
    login = LoginPage()
    login.login_page('http://172.18.1.187/#/login')
    login.input_username('root')
    login.input_password('111111')
    login.clcik_submit()