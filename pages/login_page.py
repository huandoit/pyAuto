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

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """ 登录页面 """

    # def __init__(self):
    #     """ 初始化浏览器 """
    #     self.driver = webdriver.Chrome()
    #     self.url = 'http://172.18.1.187/#/login'
    #     self.driver.get(self.url)

    """ 登录页控件 """
    username_input = (By.XPATH, '//input[@placeholder="用户名"]')
    password_input = (By.XPATH, '//input[@placeholder="密码"]')
    submit_btn = (By.XPATH, '//button[@type="submit"]')
    error_msg = (By.XPATH, '//div[@id="root"]/div/div[1]/span[2]')

    """ 登录后首页控件 """
    root_btn = (By.XPATH, '//div[@id="ant-header"]/ul/li[2]/a')

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
        time.sleep(2)

    def get_username(self):
        """ 获取登录后右上角的用户名称 """
        username_text = self.driver.find_element(*self.root_btn).text
        return username_text

    def get_errorinfo(self):
        """ 登录失败获取错误提示信息 """
        msg = self.driver.find_element(*self.error_msg).text
        return msg


if __name__ == '__main__':
    login = LoginPage()
    login.login_page('http://172.18.1.187/#/login')
    login.input_username('root')
    login.input_password('222222')
    login.clcik_submit()
    # print(login.get_username())
    print(login.get_errorinfo())
