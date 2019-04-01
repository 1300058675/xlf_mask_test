from page.login_page import Login_url,Login
from Common.Base.base import browser
def sign_in(username,password):
    driver = browser()
    driver.get(Login_url)
    driver.maximize_window()
    XieFun = Login(driver)
    XieFun.username(username)
    XieFun.password(password)
    XieFun.button()
if __name__ == '__main__':
    sign_in('18782048160','admin123')