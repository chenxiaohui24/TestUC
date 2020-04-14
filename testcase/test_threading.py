import threading
from selenium.webdriver import Remote
import time,unittest

# class Test_Baidu(unittest.TestCase):
def test_baidu(host, browser):
    print('当前浏览器是%s,启动时间是%s'  %  (browser,time.ctime()))
    dc = {'browserName': browser}
    driver = Remote(command_executor=host,
                    desired_capabilities=dc)
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.close()
    print('%s结束时间是%s' % (browser, time.ctime()))


if __name__=='__main__':
    lists = {'http://127.0.0.1:4444/wd/hub':'chrome','http://127.0.0.1:5555/wd/hub':'firefox'}
    threads = []
    files = range(len(lists))
    for host, browser in lists.items():
        t = threading.Thread(target=test_baidu,args=(host, browser))
        threads.append(t)

    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

