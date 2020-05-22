# -*- coding:utf-8 -*-
# Author  : tanrunjie
# Date    : 2020-05-20
# Version : v1.0
# License : MIT

from selenium import webdriver
import selenium.common.exceptions as eps
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time, random, json


class autoFill(object):

    def __init__(self, executable_path, url, options=webdriver.ChromeOptions()):
        """  初始化webdriver
        :param executable_path: chrome_driver的执行文件位置
        :param url:             网页地址
        :param options:         使用chrome的默认设置
        :return : void
        """
        self.executable_path = executable_path
        self.url = url
        self.driver = webdriver.Chrome(
            executable_path=executable_path, chrome_options=options)

    def driver_login(self, username, password):
        """  自动登录BIP
        :param username: BIP用户名
        :param password: BIP密码
        :return : void
        """
        try:
            self.driver.get(self.url)

            self.driver.find_element_by_css_selector(
                "input#j_username.inputLogin").send_keys(username)
            self.driver.find_element_by_css_selector(
                "input#j_password.inputLogin").send_keys(password)
 
            self.driver.find_element_by_css_selector("button.white.loginBt").click()

        except eps.WebDriverException:
            print("Server got error, restart before close all the test chromes, also possible firefox plug-ins.")
        except eps.NoSuchElementException:
            print("Cant find the element.")
            pass
        else:
            print("Login Success!")
        finally:
            time.sleep(4)  # 等待表格页面载入信息

    def fill_table(self, temperature, address):
        """  自动填写一日一报
        :param temperature: 当日体温
        :param address:     详细地址
        :return : void
        """

        # Buttons
        try:
            btns = self.driver.find_elements_by_xpath(
                '//input[@class="ivu-radio-input" and @type="radio"]')

            # 分析前端代码,找到对应按钮位置并click
            btns[0].click()
            btns[6].click()
            btns[8].click()
            btns[9].click()
            btns[13].click()
            btns[24].click()
            btns[32].click()
            btns[36].click()
            btns[53].click()

        except eps.InvalidElementStateException:
            print("Element maybe invisible, readonly or point to a wrong element.")
        else:
            print("Clicked all buttons correctly!")
        finally:
            time.sleep(2)  # 等待展开隐藏项
        
        # Texts
        try:
            self.driver.find_element_by_xpath(
                '//input[@placeholder="例36.8，注：>=37.3为发烧"]').send_keys(temperature)

            # 日期控件填写
            js1 = 'document.getElementsByClassName("bgy-input")[3].removeAttribute("readonly");'
            self.driver.execute_script(js1)
            self.driver.find_elements_by_xpath(
                '//input[@class="bgy-input" and @placeholder="点击选择日期"]')[1].send_keys("2018-05-01")

            # 详细地址填写
            js1 = 'document.getElementsByClassName("ivu-input ivu-input-default")[0].removeAttribute("readonly");'
            self.driver.execute_script(js1)

            addr = self.driver.find_element_by_xpath(
                '//input[@class="bgy-input" and @placeholder="填写详细地址"]')
            addr.send_keys(address)


            # 地址控件的自动点选

            # province = self.driver.find_elements_by_xpath(
            #     '//input[@class="ivu-input ivu-input-default" and @placeholder="请选择"]')[0].send_keys('广东省 / 佛山市 / 顺德区')
            # province = self.driver.find_element_by_xpath('//ul[@class = "ivu-select-dropdown-list"]/li/span')
            # self.driver.execute_script("arguments[0].textContent = '广东省 / 佛山市 / 顺德区' " , province)
            self.driver.find_elements_by_xpath(
                  '//input[@class="ivu-input ivu-input-default" and @placeholder="请选择"]')[0].click()
            time.sleep(1)
            province = self.driver.find_elements_by_xpath('//li[@class="ivu-cascader-menu-item" and contains(text(),"广东省" )]')[0]
            self.driver.execute_script("arguments[0].scrollIntoView();", province)
            time.sleep(1)
            province.click()
            time.sleep(1)
            city = self.driver.find_elements_by_xpath('//li[@class="ivu-cascader-menu-item" and contains(text(),"佛山市")]')[0]
            self.driver.execute_script("arguments[0].scrollIntoView();", city)
            time.sleep(1)
            city.click()
            district = self.driver.find_elements_by_xpath('//li[@class="ivu-cascader-menu-item" and contains(text(),"顺德区")]')[0]
            self.driver.execute_script("arguments[0].scrollIntoView();", district)
            time.sleep(1)
            district.click()

        except eps.InvalidElementStateException:
            print("Complicated wigets contains invisible Element, readonly or point to a wrong element.")
        except eps.JavascriptException:
            print("the javascript command is invalid.")
        
        else:
            print("Fill all the text contents correctly!")
        
        print('Finished Table AutoFill.')


def temperature_generate():
    fraction = random.uniform(0, 1)
    fraction = round(fraction, 1)
    temperature = 36 + fraction
    return str(temperature)

if __name__ == '__main__':
    
    with open('personal.json', 'r', encoding='utf-8') as f:
        data = json.load(f)    
   
    auto = autoFill(data['executable_path'], data['web_url'])
    auto.driver_login(data['username'], data['password'])
    auto.fill_table(temperature_generate(), data['address'])
