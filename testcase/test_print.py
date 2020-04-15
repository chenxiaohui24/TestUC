import unittest

class TESTPRINT(unittest.TestCase):
    def testprint(self):
        print('Hello, World!')


if __name__=='__mian__':
    # unittest.main()
    TESTPRINT().testprint()