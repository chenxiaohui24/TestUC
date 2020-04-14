import unittest,os
from common import basepath

suite=unittest.TestLoader().discover(start_dir=os.path.join(basepath,'testcase'),
                                     pattern='test*.py',
                                     top_level_dir=None)


if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)