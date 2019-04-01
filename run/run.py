import unittest
from BeautifulReport import BeautifulReport
import time


now_time = time.strftime('%Y-%m-%d_%H_%M_%S')
f = "..\\Report"

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../case/TaskListTest', '*_test.py')
    result = BeautifulReport(test_suite)

    result.report(filename = '任务管理测试报告'+now_time+'', description = '任务管理模块测试', log_path = f)
