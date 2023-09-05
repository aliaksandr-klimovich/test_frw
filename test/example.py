"""
This module is for debugging purposes and presented as lightweight example.
"""

from case import TestCase
from const import TestVerdict
from runner import TestRunner


class CustomTestCase1(TestCase):
    def run(self):
        self.assert_eq(True, True)


class CustomTestCase2(TestCase):
    def run(self):
        print('checking that passed test case does not crush')
        self.assert_eq(True, True)

        print('checking that failed result is stored and test case does not stuck here')
        self.check_eq(False, True, 'shall not raise')

        print('checking that failed result leads to aborting test run')
        self.assert_eq(False, True)

        print('this log should not be printed')
        self.check_eq(True, True)


results = TestRunner.run(CustomTestCase1, CustomTestCase2)
assert results[0].verdict is TestVerdict.PASSED
assert results[1].verdict is TestVerdict.FAILED
