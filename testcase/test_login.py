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
import time
from pages.login_page import LoginPage


class TestLogin(object):

    def setup_class(self):
        """ 在所有用例执行前初始化浏览器"""
        self.login = LoginPage()
        self.login.open('http://172.18.1.187/#/login')

    def teardown(self):
        """ 每个登录测试执行后执行清空输入框操作 """
        self.login.clear(self.login.username_input)
        self.login.clear(self.login.password_input)
        time.sleep(2)

    def teardown_class(self):
        """ 所有用例执行完后关闭浏览器 """
        self.login.driver.quit()

    def test_correct_username_password(self):
        """ 正确的用户名和密码 """
        self.login.input_username('root')
        self.login.input_password('111111')
        self.login.clcik_submit()
        assert self.login.get_username() == 'root'
        self.login.logout()

    def test_correct_username_wrong_password(self):
        """ 正确的用户名、错误的密码 """
        self.login.input_username('root')
        self.login.input_password('222222')
        self.login.clcik_submit()
        assert self.login.get_errorinfo() == '用户名或密码不正确，请重新输入！'

    def test_wrong_username_password(self):
        """ 不存在的用户名和密码 """
        self.login.input_username('123456')
        self.login.input_password('222222')
        self.login.clcik_submit()
        assert self.login.get_errorinfo() == '用户名或密码不正确，请重新输入！'

    def test_none_username_password(self):
        """ 不输入用户名或密码 """
        self.login.input_username('')
        self.login.input_password('')
        self.login.clcik_submit()
        assert self.login.get_errorinfo() == '用户名或密码不能为空'


if __name__ == '__main__':
    pytest.main()
