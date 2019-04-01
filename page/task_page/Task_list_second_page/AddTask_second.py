# coding=utf-8
from Common.Base.base import Base
from selenium import webdriver
from page.login_page.login import Login
from time import sleep
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys

Login_url = 'https://c.xielifun.com/#/login'

# 在项目管理按钮
loc_project_management = ('xpath', '/html/body/div/aside/div/ul/div/li[3]/div')
# 在建项目页面
loc_projecting = ('xpath', '/html/body/div/aside/div/ul/div/li[3]/ul/div/li[1]')
# 选择第一个项目
loc_projecting_1 = ('xpath', '/html/body/div/div[2]/main/div/div/div/div[2]/div[1]/div[1]/a/div')

# 二期任务列表管理button
loc_task = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/div')
# 二期任务列表button
loc_task_list = ('xpath', '/html/body/div/aside/div/ul/div/li[4]/ul/div/li[1]')

# 任务名称获取
loc_release_name = ('xpath', '//*[@id="pane-all"]/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div')


# 发布任务按钮
loc_addtask = ('xpath', '//*[@id="pane-all"]/div/div[2]/div[1]/div/button[1]')

# 任务名称
loc_taskname = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[1]/div/div/input')

# 任务内容
loc_tasktext = ('class name', 'el-textarea__inner')

# 任务类型
loc_tasktype = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[4]/div/div/div[1]/input')
# 任务类型选择
loc_choose_tasktype = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]')

# 紧急程度定位
loc_emergency = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[5]/div/div/div[1]/input')
# 紧急程度选择
loc_choose_emergency = ('xpath', '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

# 负责人定位
loc_head = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[6]/div/div/div[1]/input')
# 负责人选择
loc_choose_head = ('xpath', '/html/body/div[5]/div[1]/div[1]/ul/li[1]')

# 参与人定位
loc_part = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[7]/div/button')
# 参与人选择
loc_choose_part = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[2]/div/div[2]/div/form/div/div[1]/h3/label/span/span')
# 参与人添加按钮
loc_add_part = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[2]/div/div[2]/div/form/div/div[2]/p[1]/button')
# 参与人页面确认
loc_part_confirm = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[2]/div/div[3]/span/button')

# 截至时间定位
loc_time = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[8]/div/div/input')
# 发布按钮
loc_release = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[3]/span/button[2]')
# 存草稿
loc_draft = ('class name', 'el-button el-button--cancel el-button--medium')
# 文件上传
loc_file = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[9]/div/div/div[1]/div[1]/button')
# 取消按钮
loc_cancel_button = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[3]/span/button[1]')

# 任务名称断言
loc_assert_name = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[1]/div/div[2]')
# 任务内容断言
loc_assert_content = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[3]/div/div[2]')
# 任务类型断言
loc_assert_type = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[4]/div/div[2]')
# 紧急程度断言
loc_assert_emergency = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[5]/div/div[2]')
# 负责人断言
loc_assert_head = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[6]/div/div[2]')
# 截止时间断言
loc_assert_time = ('xpath', '//*[@id="pane-all"]/div/div[11]/div[1]/div/div[2]/form/div[8]/div/div[2]')

# 三方键盘库
keyboard = Controller()


class AddTask_second(Base):

    def to_project_management(self):
        '''前往项目管理页面'''
        self.click(loc_project_management)

    def to_projecting(self):
        '''前往第一个在建项目页面'''
        self.click(loc_projecting)
        self.click(loc_projecting_1)

    def to_second_task_list(self):
        '''前往二期任务列表页面'''
        sleep(1)
        self.to_projecting()
        self.switch_to_window(1)
        self.click(loc_task)
        sleep(1)
        self.click(loc_task_list)

    def assert_release(self):
        '''获取任务发布后的名称，作为断言信息(一期页面使用)'''
        a = self.get_text(loc_release_name)
        self.driver.close()
        sleep(1)
        self.switch_to_window(0)
        print('页面值：'+a)
        return a

    def switch_to_window_and_close(self):
        self.switch_to_window(0)
        sleep(1)
        self.switch_to_window(1)
        sleep(1)
        self.driver.close()
        sleep(1)
        self.switch_to_window(0)
        sleep(1)

    def assert_one_release(self):
        '''获取任务发布后的名称，作为断言信息（二期页面使用）'''
        sleep(1)
        a = self.get_text(loc_release_name)
        print('页面值：'+a)
        return a

    '''
    这里是抄的
    '''
    def click_addtask(self):
        '''定位任务列表添加任务按钮'''
        self.click(loc_addtask)

    def set_taskname(self, name):
        '''添加任务页面，任务名称'''
        self.clear(loc_taskname)
        self.sendKeys(loc_taskname, name)

    def set_tasktext(self, text):
        '''添加任务页面，任务名内容'''
        self.sendKeys(loc_tasktext, text)

    def set_tasktype(self):
        '''点击任务类型'''
        self.click(loc_tasktype)
        sleep(1)
        # self.click(loc_choose_tasktype)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_emergency(self):
        '''点击任务类型'''
        self.click(loc_emergency)
        sleep(1)
        # self.click(loc_choose_emergency)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_head(self):
        '''点击负责人'''
        self.click(loc_head)
        sleep(1)
        # self.click(loc_choose_head)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_part(self):
        '''参与人定位'''
        self.click(loc_part)
        self.click(loc_choose_part)
        self.click(loc_add_part)
        self.click(loc_part_confirm)

    def set_time(self, time):
        '''设置截至时间'''
        self.sendKeys(loc_time, time)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def set_release(self):
        '''发布按钮'''
        js = 'document.getElementsByClassName("el-button el-button--primary el-button--medium")[16].click();'
        sleep(1)
        self.driver.execute_script(js)

    def set_draft(self):
        '''保存为草稿'''
        js = 'document.getElementsByClassName("el-button el-button--primary el-button--medium")[17].click();'
        sleep(1)
        self.driver.execute_script(js)

    def assert_name(self):
        '''获取名称提示文本'''
        self.scroll_bar_Specified_element(loc_taskname)
        sleep(1)
        a = self.get_text(loc_assert_name)
        print('页面名称输入框提示：' + a)
        return a

    def assert_content(self):
        '''获取内容提示文本'''
        self.scroll_bar_Specified_element(loc_taskname)
        sleep(1)
        a = self.get_text(loc_assert_content)
        print('页面内容输入框提示：' + a)
        return a

    def assert_type(self):
        '''获取任务类型提示文本'''
        sleep(1)
        a = self.get_text(loc_assert_type)
        print('页面任务类型提示：' + a)
        return a

    def assert_emergency(self):
        '''获取任务紧急情况提示文本'''
        sleep(1)
        a = self.get_text(loc_assert_emergency)
        print('页面紧急情况提示：' + a)
        return a

    def assert_head(self):
        '''获取任务紧急情况提示文本'''
        sleep(1)
        a = self.get_text(loc_assert_head)
        print('页面负责人提示：' + a)
        return a

    def assert_time(self):
        '''获取时间提示文本'''
        sleep(1)
        a = self.get_text(loc_assert_time)
        print('页面时间输入框提示：' + a)
        return a

    def clear_taskname(self):
        '''清除名称输入框文本'''
        a = self.find_element(loc_taskname)
        a.send_keys(Keys.CONTROL, 'a')
        a.send_keys(Keys.BACKSPACE)

    def multiple_button(self):
        '''多任务按钮'''
        self.click(lco_multiple_button)

    def cancel_button(self):
        '''取消按钮'''
        self.click(loc_cancel_button)

    def add_task(self, name, text, time, key_0=False, key_1=True, key_2=True, key_3=True, key=2):
        '''发布任务'''
        self.set_taskname(name)
        # 如果key_0为true，则执行多任务按钮
        if key_0:
            self.multiple_button()
        self.set_tasktext(text)
        # 如果key_1为true，则选择任务类型
        if key_1:
            self.set_tasktype()
        self.scroll_bar_Specified_element(loc_file)
        # 如果key_2为true，则选择紧急程度
        if key_2:
            self.set_emergency()
        # 如果key_3为true，则选择负责人
        if key_3:
            self.set_head()
        self.set_part()
        self.set_time(time)
        sleep(1)
        # 如果key为true，则点击发布任务，否则点击存为草稿
        if key==1:
            print('正在取消发布')
            self.cancel_button()
        elif key==2:
            print('正在发布任务')
            self.set_release()
        else:
            print('正在保存为草稿')
            self.set_draft()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(Login_url)
    driver.maximize_window()
    a = Login(driver)
    b = AddTask_second(driver)
    a.login(18280199940, 'admin123')
    b.to_project_management()
    b.to_second_task_list()
    b.click_addtask()
    b.add_task('12', '123', '2019/3/20')