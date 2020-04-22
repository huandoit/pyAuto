#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/21 17:19
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : test_login.py
@Software: PyCharm
@description: 登录testcase
"""

import pytest
from pages.login_page import LoginPage


class TestLogin(object):

    def setup_class(self):
        """ 在所有用例执行前初始化浏览器"""
        self.login = LoginPage()
        self.login.open('http://172.18.1.187/#/login')

    def teardown(self):
        """ 每个登录测试执行后执行登出操作 """
        self.login.logout()

    def test_correct_username_password(self):
        """ 正确的用户名和密码 """
        self.login.input_username('root')
        self.login.input_password('111111')
        self.login.clcik_submit()
        assert self.login.get_username() == 'root'
