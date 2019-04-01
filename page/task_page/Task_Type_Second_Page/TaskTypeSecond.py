from Common.Base.base import Base
from selenium import webdriver
from page.login_page.login import Login
from time import sleep
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

Login_url = 'https://c.xielifun.com/#/login'

# 在项目管理按钮
loc_project_management = ('xpath', '/html/body/div/aside/div/ul/div/li[3]/div')
# 在建项目页面
loc_projecting = ('xpath', '/html/body/div/aside/div/ul/div/li[3]/ul/div/li[1]')
# 选择第一个项目
loc_projecting_1 = ('xpath', '/html/body/div/div[2]/main/div/div/div/div[2]/div[1]/div[1]/a/div')
# 二期任务列表管理button
loc_task = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/div')


# 类型列表
loc_tasktype = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/ul/div/li[2]')
# 添加类型按钮
loc_addtype = ('xpath', '/html/body/div/div[2]/main/div/div[2]/div[1]/button[1]')
# 类型删除按钮
loc_typedelete = ('xpath', '/html/body/div/div[2]/main/div/div[2]/div[1]/button[3]')

# 类型名称输入框
loc_typename = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[2]/form/div[1]/div/div/input')

# 类型内容输入框
loc_typetext = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[2]/form/div[2]/div/div/textarea')

# 加分按钮
loc_upgrade = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[2]/form/div[3]/div/div[1]/div/div/div/span[2]')

# 减分按钮
loc_downgrade = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[2]/form/div[3]/div/div[2]/div/div/div/span[2]')

# 确定提交按钮
loc_typesubmit = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[3]/span/button[2]')
# 取消提交按钮
loc_typecancel = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[3]/span/button[1]')

# 名称断言
loc_assert_name = ('xpath', '/html/body/div[1]/div[2]/main/div/div[5]/div/div[2]/form/div[1]/div/div[2]')

# 发布功能断言
loc_assert_type_name = ('xpath', '/html/body/div/div[2]/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div')


# 删除任务类型按钮
loc_type_delete = ('xpath', '/html/body/div/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/button[2]/span/i')
# 删除任务类型确定按钮
loc_type_delete_submit = ('xpath', '/html/body/div[2]/div/div[3]/button[2]')
#
loc_type_delete_cancel = ('xpath', '/html/body/div[2]/div/div[3]/button[1]')

# 查看按钮
loc_view_type = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div/span/button')
# 查看内容按钮功能
loc_view_content_type = ('xpath', '/html/body/div[3]')

# 编辑按钮
loc_editor_type = ('xpath', '/html/body/div[1]/div[2]/main/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/button[1]')

class TaskTypeSecond(Base):

    def to_project_management(self):
        '''前往项目管理页面'''
        self.click(loc_project_management)

    def to_projecting(self):
        '''前往第一个在建项目页面'''
        self.click(loc_projecting)
        self.click(loc_projecting_1)

    def to_second_task_type(self):
        '''前往二期任务列表页面'''
        sleep(1)
        self.to_projecting()
        self.switch_to_window(1)
        self.click(loc_task)
        sleep(1)
        self.click(loc_tasktype)

    def click_tasktype(self):
        '''点击任务类型'''
        sleep(1)
        self.click(loc_tasktype)

    def click_addtype(self):
        '''点击添加任务类型'''
        self.click(loc_addtype)

    def click_deletetype(self):
        '''点击删除任务类型'''
        self.click(loc_deletetype)

    def click_typesubmit(self):
        '''点击确定提交类型按钮'''
        self.click(loc_typesubmit)

    def click_typecancel(self):
        '''点击取消提交类型按钮'''
        self.click(loc_typecancel)

    def set_typename(self, name):
        '''添加任务名称'''
        self.clear(loc_typename)
        self.sendKeys(loc_typename, name)

    def set_typetext(self, text):
        '''点击任务描述'''
        self.clear(loc_typetext)
        sleep(1)
        self.sendKeys(loc_typetext, text)

    def set_upgrade(self):
        '''设置加分'''
        self.click(loc_upgrade)

    def set_downgrade(self):
        '''设置减分'''
        self.click(loc_downgrade)

    def to_type_list(self):
        '''前往任务类型页面'''
        self.click(loc_task)
        sleep(1)
        self.click(loc_tasktype)

    def assert_name(self):
        '''类型名称断言'''
        sleep(1)
        a = self.get_text(loc_assert_name)
        print('页面值：'+a)
        return a

    def assert_submit(self):
        '''提交功能断言'''
        sleep(1)
        a = self.get_text(loc_assert_type_name)
        print('页面值：'+a)
        return a

    def delete_type(self, key = True):
        '''删除类型按钮'''
        sleep(1)
        self.click(loc_type_delete)
        sleep(1)
        if key:
            self.click(loc_type_delete_submit)
        else:
            self.click(loc_type_delete_cancel)

    def click_editor_type(self):
        '''编辑按钮'''
        sleep(1)
        self.click(loc_editor_type)

    def clear_typename(self):
        '''清除名称输入框文本'''
        a = self.find_element(loc_typename)
        a.send_keys(Keys.CONTROL, 'a')
        a.send_keys(Keys.BACKSPACE)

    def add_type(self, name, text, key=True):
        self.set_typename(name)
        self.set_typetext(text)
        self.set_upgrade()
        self.set_downgrade()
        if key:
            print('点击确定')
            self.click_typesubmit()
        else:
            print('点击取消')
            self.click_typecancel()

    # def get_type_content(self):
    #     sleep(1)
    #     self.click(loc_view_type)
    #     sleep(1)
    #     js = 'document.getElementsByClassName("el-popover el-popper el-popover--plain")[14].value;'
    #     sleep(1)
    #     a = self.driver.execute_script(js)
    #     print(a)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(Login_url)
    driver.maximize_window()
    a = Login(driver)
    b = TaskTypeSecond(driver)
    a.login(18280199940, 'admin123')
    b.to_project_management()
    b.to_second_task_type()
    b.click_addtype()
    b.add_type('a', 'b', 2, True)
