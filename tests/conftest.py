import pytest
from tests.homework import Rectangle


@pytest.fixture
def rectangle():
    return Rectangle(width=3, height=4)
