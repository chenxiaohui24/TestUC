from common import Readfile
import ddt,unittest,time
from common import xlsxpath


testdata=Readfile(xlsxpath).readxlsx()
@ddt.ddt
class YMDD(unittest.TestCase):
    @ddt.data(*testdata)
    def test_print(self,data):
        print('现在时间是:%s' % time.ctime() +' 这个孩子的名字叫'+data['name']+'。')
        time.sleep(3)

if __name__=='__main__':
    unittest.main()

