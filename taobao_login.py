# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class taobao_infos:

    # 初始化
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs",{"profile.managed_default_content_settings:image":2})# 不加载图片
        options.add_experimental_option('excludeSwitches',['enable-automation'])# 以开发者模式启动

        self.browser = webdriver.Chrome(executable_path=chromedriver_path , options=options)
        self.wait = WebDriverWait(self.browser,10)

    
    def login(self):

        # 打开网页
        self.browser.get(self.url)
        
        # 点击微博登录按钮
        password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.weibo-login')))
        password_login.click()

        # 键入微博账号
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.username > .W_input ')))
        weibo_user.send_keys(weibo_username)

        # 键入微博密码
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.password > .W_input ')))
        weibo_pwd.send_keys(weibo_password)

        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.J_MemberNick member-nick')))
        print(taobao_name.text)
        


if __name__ == "__main__":
    
    chromedriver_path = "C:/Users/10338/AppData/Local/Programs/Python/Python38/Scripts/chromedriver.exe"
    weibo_username = "123456"
    weibo_password = "123456"

    a = taobao_infos()
    a.login()

