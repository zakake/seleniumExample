import unittest
from myModule import is_prime


class SampleTestcase(unittest.TestCase):
    def prime_test(self):
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()
