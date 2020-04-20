#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/16 11:00
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : usermanager_page.py
@Software: PyCharm
@description: 用户管理
"""

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserPage(BasePage):
    """ 用户管理页面，包括用户、用户组和部门三个tab """

    # def __init__(self):
    #     """ 初始化浏览器 """
    #
    #     self.driver = webdriver.Chrome()
    #     # 登录
    #     self.driver.get('http://172.18.1.187/#/login')
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[2]/div/input').send_keys('root')
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[3]/div/input').send_keys('111111')
    #     self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/form/div[4]/button').click()
    #     time.sleep(5)
    #
    #     self.url = 'http://172.18.1.187/#/system'
    #     self.driver.get(self.url)

    """ 用户tab页下控件 """
    adduser_btn = (By.XPATH, '//a[@title="部门"]')

    """ 添加用户窗口下控件 """
    cluster_select = (By.XPATH, '//div[@title="cluster1"]')
    # 所有输入框
    input = (By.XPATH, '//div[@class="col-sm-9"]/input')
    sex_radio = (By.XPATH, '//input[@type="radio"]')

    def user_page(self, url):
        """ 进入用户管理页面 """
        self.login('root', '111111')
        self.open(url)

    def clcik_adduser(self):
        """ 点击“添加用户”按钮 """
        # element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[3]/div/div/div/div[1]/ul/li[3]/a')
        # element.click()
        self.find_element(*self.adduser_btn).click()
        time.sleep(2)

    def select_cluster(self, index):
        """
        在添加用户窗口中选择集群
        :param index:选择下拉列表中的第几个集群
        :return:
        """
        cluster_index = (By.XPATH, f'//div[@class="col-sm-9"]/div[2]/div/div/div/ul/li[{index}]')

        self.find_element(*self.cluster_select).click()
        time.sleep(2)
        self.find_element(*cluster_index).click()

    def input_username(self, username):
        """ 在添加用户窗口中输入用户名称 """
        username_input = self.find_elements(*self.input)[0]
        username_input.send_keys(username)

    def input_realname(self, realname):
        """ 在添加用户窗口中输入真实姓名 """
        self.find_elements(*self.input)[1].send_keys(realname)

    def select_sex(self, index):
        """
        选择性别
        :param index: 0 男，1 女
        :return:
        """
        self.driver.find_elements(*self.sex_radio)[index].click()


if __name__ == '__main__':
    user_page = UserPage()
    user_page.user_page('http://172.18.1.187/#/system')
    user_page.clcik_adduser()
    user_page.select_cluster(2)
    user_page.input_username("wanghuan")
    user_page.input_realname("wanghuan")
    user_page.select_sex(1)
