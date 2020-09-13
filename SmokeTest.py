import unittest
from PageMyStore import PageMyStore
import os
import HtmlTestRunner
def suite():
    suite = unittest.TestSuite()
    suite.addTest(PageMyStore('test_Search'))
    suite.addTest(PageMyStore('test_SignIn'))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
                report_title='My unit test',
                )

    runner.run(suite())