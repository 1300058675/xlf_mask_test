from Common.Base.base import Base
from selenium import webdriver
from time import sleep
Login_url = 'https://c.xielifun.com/#/login'

class Login(Base):
    loc_username = ('xpath', '/html/body/div[1]/div/div/div/form/div[1]/div/div[1]/input')#账号
    loc_password = ('xpath', '/html/body/div[1]/div/div/div/form/div[2]/div/div/input')#密码
    loc_button = ('xpath', '/html/body/div[1]/div/div/div/form/div[4]/div/button')#登陆
    loc_click = ('xpath', '/html/body/div/div[2]/span/div[3]/div[1]')

    def username(self, username):#输入账号
        self.sendKeys(self.loc_username, username)

    def password(self, password):#输入密码
        self.sendKeys(self.loc_password, password)

    def button(self):#点击登录
        self.click(self.loc_button)

    def click_button(self):
        self.click(self.loc_click)

    def login(self, user, psw):
        self.username(user)
        self.password(psw)
        self.button()
        self.click_button()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(Login_url)
#     a = Login(driver)
#     a.login(13990164894, 'admin123')
#     sleep(4)
#     driver.close()
