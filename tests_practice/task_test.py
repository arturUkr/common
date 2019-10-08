import unittest
from unittest.mock import patch
from tests_practice.task_list import (
    task_1, task_2, task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10,
    task_11, task_12, task_13, task_14, task_15, task_16, task_17, task_18, task_19,
    task_20
)


class TestTask(unittest.TestCase):

    def test_task_1(self):
        l1, l2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertListEqual(task_1(l1, l2), [1, 2, 3, 5, 8, 13])

    def test_task_2(self):
        self.assertEqual(task_2("I am a good developer. I am also a writer"), 5)

    def test_task_3(self):
        self.assertTrue(task_3(27))
        self.assertFalse(task_3(4))
        self.assertRaises(ValueError, task_3, 9.1)

    def test_task_4_equal(self):
        self.assertEqual(task_4(59), 5)
        self.assertEqual(task_4(48), 3)

    def test_task_4_notequal(self):
        self.assertNotEqual(task_4(11), 3)
        self.assertNotEqual(task_4(12), 4)

    def test_task_5_equal(self):
        self.assertEqual(task_5([0, 2, 3, 0, 4, 6, 7, 10]), [2, 3, 4, 6, 7, 10, 0, 0])
        self.assertEqual(task_5([2, 3, 4, 6, 7, 10]), [2, 3, 4, 6, 7, 10])

    def test_task_6_true(self):
        self.assertTrue(task_6([5, 7, 9, 11]))

    def test_task_6_false(self):
        self.assertFalse(task_6([5, 7, 9, 999]))

    def test_task_7_equal(self):
        self.assertListEqual(task_7([5, 3, 4, 3, 4]), [5])
        self.assertListEqual(task_7([5, 1, 3, 4, 3, 4]), [1, 5])

    def test_task_8_equal(self):
        self.assertListEqual(task_8([1, 2, 3, 4, 6, 7, 8]), [5])

    def test_task_9_equal(self):
        self.assertEqual(task_9([1, 2, 3, (1, 2), 3]), [3])
        self.assertEqual(task_9([1, 2, 3, (1, 2), 3, (1, )]), [3, 5])

    def test_task_9_notequal(self):
        self.assertNotEqual(task_9([1, 2, 3, (1, 2), 3, (1, )]), [1])

    def test_task_10_equal(self):
        self.assertEqual(task_10("Hello World and Coders"), "sredoC dna dlroW olleH")

    def test_task_10_notequal(self):
        self.assertNotEqual(task_10("Artur"), "rutr")

    def test_task_11_equal(self):
        self.assertEqual(task_11(63), "1:3")
        self.assertEqual(task_11(57), "0:57")

    def test_task_12_equal(self):
        self.assertEqual(task_12("fun&!! time"), "time")
        self.assertEqual(task_12("I love dogs"), "love")

    @patch('builtins.input', return_value="My name is Michele")
    # @patch('tests_practice.task_list.task_13', return_value="My name is Michele")
    def test_task_13_equal(self, mock):
        self.assertEqual(task_13(), "Michele is name My")

    # @patch('builtins.input', return_value="My name is Michele")
    # def test_task_13_notequal(self, mock):
    #     self.assertNotEqual(task_13(), "Michele is name My My")

    @patch("builtins.input", return_value=9)
    def test_task_14_equal(self, mock):
        self.assertListEqual(task_14(), [1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_task_15_equal(self):
        self.assertListEqual(task_15([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]), [4, 16, 36, 64, 100])

    def test_task_16_equal(self):
        self.assertEqual(task_16(4), 10)

    def test_task_17_equal(self):
        self.assertEqual(task_17(4), 24)
        self.assertEqual(task_17(5), 120)

    def test_task_18_equal(self):
        self.assertEqual(task_18("abcd"), "bcdE")

    def test_task_19_equal(self):
        self.assertEqual(task_19("edcba"), "abcde")

    def test_task_20_equal(self):
        self.assertTrue(task_20(1, 2))
        self.assertFalse(task_20(2, 1))
        self.assertEqual(task_20(1, 1), "-1")


if __name__ == '__main__':
    unittest.main()
