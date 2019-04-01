# coding=utf-8
import unittest
from selenium import webdriver
from page.login_page.login import Login
from page.task_page.Todo_Task_Page.todotestlist import TodoTask
from page.task_page.Task_List_Page.AddTask import AddTask
import ddt
from time import sleep
from Common.Data.Read_Excel import ExcelUtil
import os, time

# 设置excle文件路径
propath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
filepath = os.path.join(propath, "Data", "Task", "todotask.xlsx")
# 初始化
return_data = ExcelUtil(filepath)
run_data = ExcelUtil(filepath, 'Sheet2')
send_data = ExcelUtil(filepath, 'Sheet3')

# 撤回输入框数据
data_return = return_data.get_excel_data()
# 执行输入框数据
data_run = run_data.get_excel_data()
# 派遣输入框
data_send = send_data.get_excel_data()


@ddt.ddt
class Todo_Task_Test(unittest.TestCase):  # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.delete_all_cookies()
        print('-----------------------------------初始化环境-----------------------------------')
        self.driver.refresh()
        print('------------------------------------用例执行------------------------------------')
        self.login = Login(self.driver)
        self.todotask = TodoTask(self.driver)
        self.addtask = AddTask(self.driver)
        self.driver.get('https://c.xielifun.com/#/login')
        self.login.login(18280199940, 'admin123')
        self.todotask.to_todotasklist()

        # 获取时间戳
        self.get_time = time.strftime('%Y/%m/%d %H:%M:%S')

    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    @classmethod
    def tearDownClass(cls):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        cls.driver.close()

    def test_todobutton_run(self):
        '''验证待办按钮是否正确'''
        text = self.todotask.assert_interface()
        self.assertTrue(text == '待办任务')

    def test_toviewnrbutton_run(self):
        '''查看内容按钮是否正确'''
        self.todotask.click_viewnr()
        text = self.todotask.assert_viewnr()
        self.assertTrue(text == '内容详情')

    def test_toviewbutton_run(self):
        '''查看按钮是否正确'''
        self.todotask.click_view_button()
        text = self.todotask.assert_view()
        self.assertTrue(text == '任务详情')

    def test_runbutton_run(self):
        '''执行按钮是否正确'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1)
        self.todotask.to_todotask()
        self.todotask.click_run()
        self.todotask.run_submit_button('haha')
        text = self.todotask.assert_taskname()
        print('输入值：'+self.get_time)
        self.assertTrue(self.get_time != text)

    def test_run_cancel_run(self):
        '''取消执行按钮是否正确'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1.5)
        self.todotask.to_todotask()
        self.todotask.click_run()
        self.todotask.run_submit_button('haha', False)
        text = self.todotask.assert_taskname()
        print('输入值：'+self.get_time)
        self.assertTrue(self.get_time == text)

    def test_returnbutton_run(self):
        '''撤回按钮是否正确'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1)
        self.todotask.to_todotask()
        self.todotask.click_return()
        self.todotask.return_submit_button()
        text = self.todotask.assert_taskname()
        self.assertTrue(self.get_time != text)

    def test_return_cancel_run(self):
        '''取消撤回按钮是否正确'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1)
        self.todotask.to_todotask()
        self.todotask.click_return()
        self.todotask.return_submit_button()
        text = self.todotask.assert_taskname()
        self.assertTrue(self.get_time != text)

    @ddt.data(*data_return)
    def test_return_text_run(self, data):
        '''撤回页面，撤回原因输入框验证否正确'''
        self.todotask.click_return()
        self.todotask.return_submit_button(data['content'])
        text = self.todotask.assert_return()
        self.assertTrue(text == data['assert'])

    @ddt.data(*data_run)
    def test_run_text_run(self, data):
        '''撤回页面，撤回原因输入框验证否正确'''
        self.todotask.click_run()
        self.todotask.run_submit_button(data['content'])
        text = self.todotask.assert_run()
        self.assertTrue(text == data['assert'])

    def test_send_run(self):
        '''派遣功能正确性验证'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1)
        self.todotask.to_todotask()
        self.todotask.click_send()
        self.todotask.set_send_button('2020-03-28 14:00:08', 'text')
        self.todotask.to_todotask()
        text = self.todotask.assert_taskname()
        self.assertTrue(self.get_time != text)

    def test_send_cancel_run(self):
        '''取消派遣功能正确性验证'''
        # 添加名称为当前时间的任务
        self.addtask.click_task_name()
        self.addtask.click_addtask()
        self.addtask.clear_taskname()
        self.addtask.add_task(self.get_time, '123', '2020/3/2')
        sleep(1)
        self.todotask.to_todotask()
        self.todotask.click_send()
        self.todotask.set_send_button('2020-03-28 14:00:08', 'text', True, False)
        # self.todotask.to_todotask()
        text = self.todotask.assert_taskname()
        self.assertTrue(self.get_time == text)

    def test_send_department_run(self):
        '''派遣功能,部门为空验证'''
        # 添加名称为当前时间的任务
        self.todotask.to_todotask()
        self.todotask.click_send()
        self.todotask.set_send_button('2020-03-28 14:00:08', 'text', False, True)
        text = self.todotask.assert_department()
        self.assertTrue(text == '请选择')

    @ddt.data(*data_send)
    def test_send_time_run(self, data):
        '''派遣功能,时间输入框验证'''
        # 添加名称为当前时间的任务
        self.todotask.to_todotask()
        self.todotask.click_send()
        self.todotask.set_send_button(data['time'], 'text')
        text = self.todotask.assert_time()
        self.assertTrue(text == data['assert'])

    @ddt.data(*data_return)
    def test_send_text_run(self, data):
        '''派遣功能,任务备注输入框验证验证'''
        # 添加名称为当前时间的任务
        self.todotask.to_todotask()
        self.todotask.click_send()
        self.todotask.set_send_button('2020-03-28 14:00:08', data['content'])
        text = self.todotask.assert_text()
        self.assertTrue(text == data['assert'])

    def test_view_run_button(self):
        '''任务详情，执行任务按钮验证'''
        self.todotask.to_todotask()
        sleep(1)
        self.todotask.click_view_button()
        self.todotask.click_view_run()
        text = self.todotask.assert_view_run()
        self.assertTrue(text == '执行任务')

    def test_view_send_button(self):
        '''任务详情，派遣任务按钮验证'''
        self.todotask.to_todotask()
        sleep(1)
        self.todotask.click_view_button()
        self.todotask.click_view_send()
        text = self.todotask.assert_view_send()
        self.assertTrue(text == '派遣任务')

    def test_view_subtasks_button(self):
        '''任务详情，下发子任务任务按钮验证'''
        self.todotask.to_todotask()
        sleep(1)
        self.todotask.click_view_button()
        self.todotask.click_view_subtasks()
        text = self.todotask.assert_view_subtasks()
        self.assertTrue(text == '添加任务')

    def test_view_back_button(self):
        '''任务详情，返回任务按钮验证'''
        self.todotask.to_todotask()
        sleep(1)
        self.todotask.click_view_button()
        self.todotask.click_view_back()
        text = self.todotask.assert_view_back()
        self.assertTrue(text == '待办任务')

if __name__ == '__main__':
    unittest.main()