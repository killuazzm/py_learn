# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pyquery import PyQuery as pq
from time import sleep

class taobao_infos:
    
    # 初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs",{"profile.managed_default_contentsettings:image":2})# 不加载图片
        options.add_experimental_option('excludeSwitches',['enable-automation'])# 开发者模式启动

        self.browser = webdriver.Chrome(executable_path=chromedriver_path)
        self.wait = WebDriverWait(self.browser,50)


    # 延时操作 暂不知作用
    def sleep_and_alert(self,sec,message,is_alert):

        for second in range(sec):
            if(is_alert):
                alert = "alert(\"" + message + ":" +str(sec - second) + "秒\""
                self.browser.execute_script(alert)
                al = self.browser.switch_to.alert
                sleep(1)
                al.accept()

    # 登陆淘宝
    def login(self):

        # 跳转到淘宝登录界面
        self.browser.get(self.url)

        # 输入用户名
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('fm-login-id').send_keys(tao_username)
        
        # 输入密码
        self.browser.implicitly_wait(30)
        self.browser.find_element_by_name('fm-login-password').send_keys(tao_password)

        # 点击登录按钮
        self.browser.implicitly_wait(30)
        self.browser.find_elements_by_class_name('fm-button fm-submit password-login').click()

        # 直到获取到淘宝会员昵称才能确定登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'')))

def search_page(self):

    # 等待数据加载
    goods_total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'')))

    # 获取商品总页数

if __name__ == "__main__":

    chromedriver_path = "C:/Users/10338/AppData/Local/Programs/Python/Python38/Scripts/chromedriver.exe"
    tao_username = "123456"
    tao_password = "123456"