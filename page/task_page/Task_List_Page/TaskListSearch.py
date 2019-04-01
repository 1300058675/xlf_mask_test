from pynput.keyboard import Key, Controller
from selenium import webdriver
from Common.Base.base import Base
from page.login_page.login import Login
from page.task_page.Task_List_Page.AddTask import AddTask
from time import sleep

Login_url = 'https://c.xielifun.com/#/login'

# 类型搜索框
loc_typesearch = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[1]/div/div/div[1]/input')
# 类型搜索框清除
loc_typeclear = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[1]/div/div/div[1]/span/span/i')

# 任务状态搜索框
loc_statussearch = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[2]/div/div/div[1]/input')
# 任务状态搜索框清除
loc_statusclear= ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[2]/div/div/div[1]/span/span/i')

# 紧急程度搜索框
loc_emergencysearch = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[3]/div/div/div[1]/input')
# 紧急程度搜索框清除
loc_emergencyclear= ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[3]/div/div/div[1]/span/span/i')

# 截至时间搜索框
loc_startimesearch = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[4]/div/div/input[1]')
# 截至时间搜索框
loc_endtimesearch = ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[4]/div/div/input[2]')
# 紧急程度搜索框清除
loc_timeclear= ('xpath', '//*[@id="pane-responsible"]/div/div[1]/div/form/div[4]/div/div/i[2]')


# 三方键盘库
keyboard = Controller()

class TaskListSearch(Base):

    def set_typesearch(self, a=1):
        '''类型搜索框'''
        self.click(loc_typesearch)
        typesearch = 1
        while typesearch < a:
            typesearch +=1
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def clear_type(self):
        self.click(loc_typeclear)

    def set_statussearch(self, a=1):
        '''任务状态搜索框'''
        self.click(loc_statussearch)
        statussearch = 1
        while statussearch < a:
            statussearch+=1
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def clear_status(self):
        self.click(loc_statusclear)

    def set_emergencysearch(self, a=1):
        '''紧急程度搜索框'''
        self.click(loc_emergencysearch)
        emergencysearch = 1
        while emergencysearch < a:
            emergencysearch+=1
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def clear_emergency(self):
        self.click(loc_emergencyclear)

    def set_tasklist_timesearch(self, strtime, endtime):
        self.sendKeys(loc_startimesearch, strtime)
        self.sendKeys(loc_endtimesearch, endtime)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def clear_time(self):
        self.click(loc_timeclear)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Login_url)
    a = Login(driver)
    b = AddTask(driver)
    c = TaskListSearch(driver)
    a.login(13990164894, 'admin123')
    b.to_addtask()
    sleep(2)
    c.set_emergencysearch(3)
    c.set_statussearch(2)
    c.set_typesearch(2)
    c.set_tasklist_timesearch('2019/6/7', '2019/6/9')
    c.clear_type()
    c.clear_status()
    c.clear_time()
    c.clear_emergency()
