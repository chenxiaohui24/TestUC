import threading
import unittest
from common import test_baidu
import warnings

class Test_Baidu(unittest.TestCase):
    def test_Threading(self):
        warnings.simplefilter("ignore", ResourceWarning)
        lists = {'http://127.0.0.1:4444/wd/hub': 'chrome', 'http://127.0.0.1:5555/wd/hub': 'firefox'}
        threads = []
        files = range(len(lists))
        for host, browser in lists.items():
            t = threading.Thread(target=test_baidu, args=(host, browser))
            threads.append(t)

        for i in files:
            threads[i].start()
        for i in files:
            threads[i].join()


if __name__=='__main__':
    unittest.main()