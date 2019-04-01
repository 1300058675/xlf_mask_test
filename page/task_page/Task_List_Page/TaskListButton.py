from selenium import webdriver

from Common.Base.base import Base
from page.login_page.login import Login
from page.task_page.Task_List_Page.AddTask import AddTask
from time import sleep

Login_url = 'https://c.xielifun.com/#/login'

# 查看任务内容按钮
loc_review = ('xpath', '//*[@id="pane-responsible"]/div/div[3]/div[1]/div[3]/table/tbody/tr/td[4]/div/button')
loc_reviewtask = ('xpath', '//*[@id="pane-responsible"]/div/div[3]/div[3]/div/div[2]/p')
# loc_reviewtask = ('class name', 'el-dialog__body')

# 批量删除删除草稿按钮
loc_all_delete = ('xpath', '//*[@id="pane-all"]/div/div[2]/div[1]/div/button[3]')
# 批量发布草稿按钮
loc_all_release = ('xpath', '//*[@id="pane-all"]/div/div[2]/div[1]/div/button[2]')

# 单独发布按钮
loc_release = ('xpath', '//*[@id="pane-responsible"]/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[13]/div/button[2]/span/i')

# 单独删除按钮
loc_delete = ('xpath', '//*[@id="pane-responsible"]/div/div[3]/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[13]/div/button[4]/span/i')

class TaskListButton(Base):

    def TaskList_all_release(self):
        '''草稿批量发布按钮'''
        self.click(loc_all_release)

    def TaskList_all_delete(self):
        '''草稿批量删除按钮'''
        self.click(loc_all_delete)

    def TaskList_contentreview(self):
        '''内容详情查看'''
        self.click(loc_review)

    def get_tasktext(self):
        return self.get_text(loc_reviewtask)

    def set_task_caogao(self):
        pass

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Login_url)
    a = Login(driver)
    sleep(1)
    b = AddTask(driver)
    c = TaskListButton(driver)
    a.login(13990164894, 'admin123')
    b.to_addtask()
    sleep(2)
    c.TaskList_review()
    d = c.get_tasktext()
    print(d)
    sleep(2)
    driver.close()