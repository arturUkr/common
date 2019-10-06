import pytest
from tests.homework import Rectangle

# moved to conftest.pys
# @pytest.fixture
# def rectangle():
#     return Rectangle(width=3, height=4)


def test_01_get_rectangle_perimeter(rectangle):
    assert rectangle.get_rectangle_perimeter() == 14


def test_02_get_rectangle_square(rectangle):
    assert rectangle.get_rectangle_square() == 12


def test_03_get_rectangle_diagonal(rectangle):
    assert rectangle.get_rectangle_diagonal() == 5


@pytest.mark.parametrize('test_input, expected', [(0, 0), (1, 90), (2, 180), (3, 270), (4, 360)])
def test_04_get_sum_of_corners(rectangle, test_input, expected):
    assert rectangle.get_sum_of_corners(test_input) == expected


def test_05_get_sum_of_corners_error(rectangle):
    with pytest.raises(ValueError):
        rectangle.get_sum_of_corners(5)


def test_07_get_radius_of_circumscribed_circle(rectangle, monkeypatch):
    def mock_return(*args):
        return 5
    monkeypatch.setattr(Rectangle, "get_rectangle_diagonal", mock_return)
    assert rectangle.get_radius_of_circumscribed_circle() == 2.5


def test_08_get_radius_of_inscribed_circle():
    rectangle = Rectangle(width=3, height=3)
    assert rectangle.get_radius_of_inscribed_circle() == 1.5


def test_09_get_radius_of_inscribed_circle_error():
    rectangle = Rectangle(width=3, height=4)
    with pytest.raises(ValueError):
        rectangle.get_radius_of_inscribed_circle()





