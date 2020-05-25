import unittest

from GC import GCContent


class MyTestCase(unittest.TestCase):
    def test_1(self):
        gc = GCContent("GC_test1.txt")
        self.assertEqual(gc.get_result()[0], "Rosalind_6839")
        self.assertAlmostEqual(gc.get_result()[1], 54.033149, 5)

    def test_2(self):
        gc = GCContent("GC_test2.txt")
        self.assertEqual(gc.get_result()[0], "Rosalind_6670")
        self.assertAlmostEqual(gc.get_result()[1], 52.205882, 5)

    def test_3(self):
        gc = GCContent("GC_test3.txt")
        self.assertEqual(gc.get_result()[0], "Rosalind_3635")
        self.assertAlmostEqual(gc.get_result()[1], 55.168884, 5)

    def test_4(self):
        gc = GCContent("GC_test4.txt")
        self.assertEqual(gc.get_result()[0], "Rosalind_1507")
        self.assertAlmostEqual(gc.get_result()[1], 51.960784, 5)

    def test_5(self):
        gc = GCContent("GC_test5.txt")
        self.assertEqual(gc.get_result()[0], "Rosalind_8997")
        self.assertAlmostEqual(gc.get_result()[1], 51.398601, 5)


if __name__ == '__main__':
    unittest.main()
