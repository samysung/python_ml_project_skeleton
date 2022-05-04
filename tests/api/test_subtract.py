""" tests.api.subtract module

"""
import pytest

from pmps.api.subtract import subtract

testdata = [
    (10, 6, 4),
    (17, 9, 8),
    (17, 29, -12)
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_add(a, b, expected):
    s = subtract(a, b)
    assert s == expected
