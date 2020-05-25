import unittest

from FIB import Fibonacci


class MyTestCase(unittest.TestCase):
    def test_1(self):
        fib = Fibonacci(5, 3)
        self.assertEqual(fib.get_result(), 19)

    def test_2(self):
        fib = Fibonacci(31, 3)
        self.assertEqual(fib.get_result(), 47079164257)

    def test_3(self):
        fib = Fibonacci(1, 5)
        self.assertEqual(fib.get_result(), 1)

    def test_seq4(self):
        with self.assertRaises(ValueError) as error:
            Fibonacci(41, 3)
        self.assertTrue(error.exception.__str__().startswith("Error:"))

    def test_seq5(self):
        with self.assertRaises(ValueError) as error:
            Fibonacci(-5, 3)
        self.assertTrue(error.exception.__str__().startswith("Error:"))


if __name__ == '__main__':
    unittest.main()
