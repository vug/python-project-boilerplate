import pytest

from helloworld import helpers


def test_math():
    assert 1 + 1 == 2, "math collapsed"


def test_raises():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_get_planet():
    assert helpers.get_planet() == "Earth", "got wrong planet"
