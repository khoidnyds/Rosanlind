import unittest

from FIBD import FibonacciDeath


class MyTestCase(unittest.TestCase):
    def test_1(self):
        fib = FibonacciDeath(6, 3)
        self.assertEqual(fib.get_result(), 4)

    def test_2(self):
        fib = FibonacciDeath(1, 3)
        self.assertEqual(fib.get_result(), 1)

    def test_3(self):
        fib = FibonacciDeath(85, 18)
        self.assertEqual(fib.get_result(), 258314806822396236)

    def test_seq4(self):
        with self.assertRaises(ValueError) as error:
            FibonacciDeath(101, 3)
        self.assertTrue(error.exception.__str__().startswith("Error:"))

    def test_seq5(self):
        with self.assertRaises(ValueError) as error:
            FibonacciDeath(50, 21)
        self.assertTrue(error.exception.__str__().startswith("Error:"))


if __name__ == '__main__':
    unittest.main()
