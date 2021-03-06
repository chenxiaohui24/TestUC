import os,csv,yaml,xlrd,time
from selenium.webdriver import Remote

basepath = os.path.dirname(__file__)
txtpath = os.path.join(basepath, 'testdata', 'txt.txt')
csvpath = os.path.join(basepath, 'testdata', 'csv.csv')
xlsxpath = os.path.join(basepath, 'testdata', 'xlsx.xlsx')
yamlpath = os.path.join(basepath, 'testdata', 'yaml.yaml')


def test_baidu(host, browser):
    print('当前浏览器是%s,启动时间是%s' % (browser, time.ctime()))
    dc = {'browserName': browser}
    driver = Remote(command_executor=host,
                    desired_capabilities=dc)
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys('selenium')
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.close()
    print('%s结束时间是%s' % (browser, time.ctime()))


class Readfile():
    def __init__(self,*args):
        self.args=args
        for self.Args in self.args:
            self.arg =self.Args

    def readtxt(self):
        with open(self.arg, 'r') as f:
            txt_file = f.readlines()
            return txt_file
            f.close()

    def readcsv(self):
        with open(self.arg, 'r') as f:
            csv_file = list(csv.reader(f))
            return csv_file
            f.close()

    def readyaml(self):
        with open(self.arg, 'r') as f:
            _yaml = f.read()
            yaml_file = yaml.safe_load(_yaml)
            return yaml_file
            f.close()

    def readxlsx(self):
        data = xlrd.open_workbook(self.arg)
        table = data.sheet_by_index(0)
        rows = table.nrows
        clos = table.ncols
        l = []
        j = 1
        for i in range(rows - 1):
            keys = table.row_values(0)
            values = table.row_values(j)
            for x in range(clos):
                d = {}
                d[keys[x]] = values[x]
                l.append(d)
            j += 1
        return l


if __name__ == '__main__':
    print(Readfile(txtpath).readtxt())
    print(Readfile(csvpath).readcsv())
    print(Readfile(yamlpath).readyaml())
    print(Readfile(xlsxpath).readxlsx())









