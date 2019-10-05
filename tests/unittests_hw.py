import unittest
from unittest.mock import patch
from tests.homework import Rectangle


class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(width=3, height=4)

    def test_01_get_rectangle_perimeter(self):
        func_result = self.rectangle.get_rectangle_perimeter()
        self.assertEqual(func_result, 14)

    def test_02_get_rectangle_square(self):
        func_result = self.rectangle.get_rectangle_square()
        self.assertEqual(func_result, 12)

    def test_03_get_rectangle_diagonal(self):
        func_result = self.rectangle.get_rectangle_diagonal()
        self.assertEqual(func_result, 5)

    def test_04_get_sum_of_corners(self):
        params_for_corner = [(0, 0), (1, 90), (2, 180), (3, 270), (4, 360)]
        for corner, expected_result in params_for_corner:
            with self.subTest(corners=corner, expected_result=expected_result):
                self.assertEqual(self.rectangle.get_sum_of_corners(corner), expected_result)

    def test_05_get_sum_of_corners_error(self):
        self.assertRaises(ValueError, self.rectangle.get_sum_of_corners, 5)  # TypeError

    def test_06_get_sum_of_corners_error_message(self):
        with self.assertRaises(ValueError) as err:
            self.rectangle.get_sum_of_corners(5)
        # self.assertTrue("Rectangle has only 4 corners" in str(err.exception))
        self.assertIn("Rectangle has only 4 corners", str(err.exception))

    @patch("tests.homework.Rectangle.get_rectangle_diagonal", return_value=5)
    def test_07_get_radius_of_circumscribed_circle(self, mock):
        func_result = self.rectangle.get_radius_of_circumscribed_circle()
        self.assertEqual(func_result, 2.5)

    def test_08_get_radius_of_inscribed_circle(self):
        instance_rectangle = Rectangle(width=3, height=3)
        func_result = instance_rectangle.get_radius_of_inscribed_circle()
        self.assertEqual(func_result, 1.5)

    def test_09_get_radius_of_inscribed_circle_error(self):
        # self.assertRaises(ValueError, self.rectangle.get_radius_of_inscribed_circle)
        with self.assertRaises(ValueError) as err:
            self.rectangle.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
