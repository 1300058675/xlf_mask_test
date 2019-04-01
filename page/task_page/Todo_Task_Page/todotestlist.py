# coding=utf-8
from Common.Base.base import Base
from selenium import webdriver
from page.login_page.login import Login
from time import sleep
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys

# 任务管理按钮
loc_task = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/div')
# 前往待办任务界面
loc_todotask = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/ul/div/li[1]')
# 断言界面
loc_aseert_to = ('xpath', '/html/body/div[1]/div[1]/nav/div[2]/div/span[2]/span[1]')
# 查看内容按钮验证
loc_viewnr_button = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/button')
# 查看内容断言验证
loc_assert_viewnr = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[3]/div/div[1]/span')
# 查看详情按钮验证
loc_view_button = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/i[1]')
# 详情页面断言验证
loc_assert_view = ('xpath', '/html/body/div/div[1]/nav/div[2]/div/span[3]/span[1]')

# 执行按钮
loc_run_button = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/i[3]')
loc_run_text = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[7]/div/div[2]/div/form/div[1]/div[2]/div/div/div/textarea')
loc_run_name_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[7]/div/div[2]/div/form/div[1]/div[2]/div/div/div[2]')
loc_run_submit = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[7]/div/div[3]/span/button[2]')
loc_run_cancel = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[7]/div/div[3]/span/button[1]')

# 撤回按钮与断言
loc_return_button = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/i[4]')
loc_return_text = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[8]/div/div[2]/div/form/div/div/div/textarea')
loc_return_submit = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[8]/div/div[3]/span/button[2]')
loc_return_cancel = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[8]/div/div[3]/span/button[1]')
loc_assert_return = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[8]/div/div[2]/div/form/div/div/div[2]')
loc_name_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div')

# 派遣按钮
loc_send_button = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[12]/div/i[2]')
# 派遣部门
loc_choose_department = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[1]/div[2]/div/div/div[1]/div[1]/input')
loc_assert_department = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[1]/div[2]/div/div/div[2]')
# 派遣人员
loc_choose_people = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]/div[1]/input')
loc_assert_people = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[2]/div[2]/div/div/div[2]')
# 派遣时间
loc_choose_time = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div[2]/div/div/div[1]/input')
loc_assert_time= ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]')
# 任务备注
loc_choose_text = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div[2]/div/div/div/textarea')
loc_assert_text = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[2]/div/form/div[4]/div[2]/div/div/div[2]')
# 派遣断言
loc_send_assert = ('xpath', '')
# 派遣取消，提交按钮
loc_send_submit = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[3]/span/button[2]')
loc_send_cancel = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[4]/div/div[3]/span/button[1]')

# 内容详情页面执行按钮
loc_view_run = ('xpath', '/html/body/div/div[2]/main/div/div[1]/div/button[1]')
loc_view_run_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[6]/div/div[1]/span')
# 内容详情页面派遣按钮
loc_view_send = ('xpath', '/html/body/div/div[2]/main/div/div[1]/div/button[2]')
loc_view_send_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[1]/span')
# 内容详情页面下发子任务按钮
loc_view_subtasks = ('xpath', '/html/body/div/div[2]/main/div/div[1]/div/button[3]')
loc_view_subtasks_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[10]/div[1]/div/div[1]/span')
# 内容详情页面返回按钮
loc_view_back = ('xpath', '/html/body/div/div[1]/nav/div[2]/div/span[2]/span[1]')
loc_view_back_assert = ('xpath', '/html/body/div/div[1]/nav/div[2]/div/span[2]/span[1]  ')
# 日志添加
loc_view_text = ('xpath', '/html/body/div/div[2]/main/div/div[4]/div[1]/button')
loc_view_text_assert = ('xpath', '/html/body/div[1]/div[2]/main/div/div[4]/div[2]/div[1]/div/div[1]/span')


Login_url = 'https://c.xielifun.com/#/login'
# 三方键盘库
keyboard = Controller()

class TodoTask(Base):

    def to_task(self):
        '''点击任务管理'''
        sleep(1)
        self.click(loc_task)

    def to_todotask(self):
        '''前往待办任务界面'''
        sleep(1)
        self.click(loc_todotask)

    def to_todotasklist(self):
        self.to_task()
        self.to_todotask()

    def assert_interface(self):
        '''查看是否成功进入待办任务页面'''
        sleep(1)
        a = self.get_text(loc_aseert_to)
        print('页面值：'+a)
        return a

    def click_viewnr(self):
        sleep(1)
        self.click(loc_viewnr_button)

    def assert_viewnr(self):
        '''查看是否进入查看页面'''
        sleep(1)
        a = self.get_text(loc_assert_viewnr)
        print('页面值：' + a)
        return a

    def click_view_button(self):
        '''点击进入任务详情页面'''
        sleep(1)
        self.click(loc_view_button)

    def assert_view(self):
        '''获取详情页面text'''
        sleep(1)
        a = self.get_text(loc_assert_view)
        print('页面值：' + a)
        return a

    def click_return(self):
        '''点击撤回按钮'''
        sleep(1)
        self.click(loc_return_button)

    def assert_return(self):
        '''断言输入框提示'''
        sleep(1)
        a = self.get_text(loc_assert_return)
        print('页面值：' + a)
        return a

    def return_submit_button(self, text='', key=True):
        '''默认确定撤回，如果key为False，则取消撤回'''
        self.sendKeys(loc_return_text, text)
        if key:
            self.click(loc_return_submit)
        else:
            self.click(loc_return_cancel)

    def assert_taskname(self):
        '''获取第一行任务名称'''
        sleep(2)
        a = self.get_text(loc_name_assert)
        print('页面值：' + a)
        return a

    def click_run(self):
        '''点击执行按钮'''
        sleep(1)
        self.click(loc_run_button)

    def assert_run(self):
        sleep(1)
        a = self.get_text(loc_run_name_assert)
        print('页面值：' + a)
        return a

    def run_submit_button(self, text, key=True):
        '''默认确定撤回，如果key为False，则取消撤回'''
        self.sendKeys(loc_run_text, text)
        if key:
            self.click(loc_run_submit)
        else:
            self.click(loc_run_cancel)

    def click_send(self):
        sleep(1)
        self.click(loc_send_button)

    def set_department(self):
        '''选择部门'''
        self.click(loc_choose_department)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_people(self):
        '''选择办理人员'''
        self.click(loc_choose_people)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_time(self, text):
        '''选择结束时间'''
        self.sendKeys(loc_choose_time, text)

    def set_text(self, text):
        '''添加任务备注'''
        self.sendKeys(loc_choose_text, text)

    def assert_department(self):
        '''获取选者部门输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_assert_department)
        print('页面值：' + a)
        return a

    def assert_time(self):
        '''获取选者时间输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_assert_time)
        print('页面值：' + a)
        return a

    def assert_text(self):
        '''获取任务备注输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_assert_text)
        print('页面值：' + a)
        return a

    def set_send_button(self,time, text, key=True, key_1=True):
        '''派遣功能'''
        if key:
            self.set_department()
        self.set_time(time)
        self.set_text(text)
        if key_1:
            self.click(loc_send_submit)
        else:
            self.click(loc_send_cancel)

    def click_view_run(self):
        self.click(loc_view_run)

    def assert_view_run(self):
        '''获取选者部门输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_view_run_assert)
        print('页面值：' + a)
        return a

    def click_view_send(self):
        self.click(loc_view_send)

    def assert_view_send(self):
        '''获取选者部门输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_view_send_assert)
        print('页面值：' + a)
        return a

    def click_view_subtasks(self):
        self.click(loc_view_subtasks)

    def assert_view_subtasks(self):
        '''获取选者部门输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_view_subtasks_assert)
        print('页面值：' + a)
        return a

    def click_view_back(self):
        self.click(loc_view_back)

    def assert_view_back(self):
        '''获取选者部门输入框提示信息'''
        sleep(1)
        a = self.get_text(loc_view_back)
        print('页面值：' + a)
        return a

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(Login_url)
    driver.maximize_window()
    a = Login(driver)
    b = TodoTask(driver)
    a.login(18280199940, 'admin123')
    b.to_task()
    b.to_todotask()
    b.click_send()
    b.set_send_button('2019/3/4', '123')
