from selenium import webdriver
from Common.Time.time import localhost_time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains    #导入鼠标事件
from time import sleep
import os

def browser(browser = 'Chrome'):
    '''打开浏览器，进行判断'''
    try:
        if browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("没有发现你所使用的浏览器,你可以使用'firefox','chrome', 'ie' 或者 'phantomjs'")
    except Exception as e:#捕获所有异常的方方法
        print("%s" % e)

class Base(object):

    def __init__(self, driver = webdriver.Chrome):
        self.driver = driver
        self.timeout = 15
        self.t = 0.5

    def find_element(self, locator):
            print(localhost_time()+'正在通过==》“'+locator[0]+'”定位元素==》“'+locator[1]+'”')
            element = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            print(localhost_time()+'“'+locator[0]+'”----“'+locator[1]+'”,定位成功')
            return element

    def find_elements(self, locator):
            print(localhost_time()+'正在通过==》“'+locator[0]+'”定位元素==》“'+locator[1]+'”')
            element = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
            print(localhost_time()+'“'+locator[0]+'”----“'+locator[1]+'”,定位成功')
            return element

    def sendKeys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def clear(self, locator):
        element = self.find_element(locator)
        element.clear()

    def is_title(self, title):
        '''判断标题(完全)，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title):
        '''判断标题（包含），返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_ElementExist(self, locator):
        '''判定元素是否存在'''
        try:
            self.find_element(locator)
            return True
        except:
            print(localhost_time()+'元素“'+locator[1]+'”不存在')
            return False

    def is_text_element(self, locator, text):
        '''判定某个元素中的text的字符是否和预期一致'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            print(localhost_time()+'元素“'+locator[1]+'”中的text和预期结果不一致')
            return False

    def get_text(self, locator):
        '''获取元素文本'''
        try:
            t = self.find_element(locator).text
            print(t)
            return t
        except:
            print(localhost_time()+'获取元素“'+locator[1]+'”文本值失败，将输出一个空字符')
            return ''

    def scroll_bar_bottom(self):
        js = "window.scrollTo(0, document.body.scrollHeight)"  # 滑动滚动条到底部
        bottom = self.driver.execute_script(js)
        return bottom

    def scroll_bar_top(self):
        js = "window.scrollTo(0,0)"  # 滑动到顶部
        top = self.driver.execute_script(js)
        return top

    def scroll_bar_left(self):
        js = "window.scrollTo(0,0)"  # 滑动到最左端
        left = self.driver.execute_script(js)
        return left

    def scroll_bar_right(self):
        js = "window.scrollTo(document.body.scrollWidth,0)"  # 滑动滚动条到最右端
        right = self.driver.execute_script(js)
        return right

    def scroll_bar_Specified_element(self, locator):
        js = "arguments[0].scrollIntoView();"  # 滑动滚动条到某个指定的元素"
        Specified_element = self.find_element(locator)
        a = self.driver.execute_script(js, Specified_element)
        return a

    def iframe_frame(self, locator):  # 切换iframe
        iframe = self.find_element(locator)  # 获取iframe
        self.driver.switch_to.frame(iframe)  # 切换至body

    def window_handles(self):
        current = self.driver.current_window_handle  # 获取当前页面
        print(current)
        all = self.driver.window_handles  # 获取全部页面
        print(all)

    def switch_to_window(self, n):
        all = self.driver.window_handles  # 获取全部页面
        self.driver.switch_to_window(all[n])  # 切换页面

    def get_tag(self, locator):
        tag = self.find_element(locator).tag_name#获取元素的标签
        return tag

    def alert(self):#弹窗
        alert = self.driver.switch_to_alert()
        return alert

    def is_alert(self):
        '''
        判断是否有alert弹窗，如果有则返回
        switch_to_alert() 定位弹窗
        text()            获取文本值
        accept()          确认
        dismiss()         取消
        send_keys()       输入值
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            # alert = self.driver.switch_to_alert()
            return result
        except:
            return False

    def alert_text(self, text):# 弹窗  text  确定  取消
        self.driver.switch_to_alert().send_keys(text)


    def mouse_flight(self, locator):#鼠标悬停
        mouse = self.find_element(locator)
        ActionChains(driver).move_to_element(mouse).perform()

    def check_box(self, locator, m, n):#复选框
        all = self.find_elements(locator)
        for i in all[m:n]:
            i.click()

    def File_upload(self,text):#文件上传,test传文件路径（.au3转换的.exe）
        relesefile = text
        os.system(relesefile)

    def Date(self, locator):
        js = "document.getElementBy"+locator[0].title()+"('"+locator[1]+"').removeAttribute('readonly');"
        self.driver.execute_script(js)

    def is_Selected(self, locator):
        '''
        判断下拉框或者按钮元素是否被选中，返回b9l值
        '''
        element = self.find_element(locator)
        result = element.is_selected()
        return result

    def drag_and_drop(self, el_locator, ta_locator):
        '''
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("locator=>#el","locator=>#ta")
        '''
        element = self.find_element(el_locator)
        target = self.find_element(ta_locator)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def clear(self, locator):
        self.find_element(locator).clear()

    def get_value(self, locator):
        '''获取文本内容'''
        try:
            t = self.find_element(locator).get_attribute('value')
            return t
        except:
            print(localhost_time()+'获取元素“'+locator[1]+'”文本值失败，将输出一个空字符')
            return ''

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('C:\\Users\\Administrator\\Desktop\\haha\\弹框.html')
    sleep(2)
    # locator('id', 'alert')
    Test = Base(driver)
    Test.click(('id', 'alert'))
    sleep(1)
    a = Test.is_alert()
    if a == False:
        print('失败')
    else:
        b = a.text()
        a.accept()
























