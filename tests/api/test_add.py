""" tests.api.add module

"""
import pytest

from pmps.api.add import add

testdata = [
    (4, 6, 10),
    (17, 9, 26),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_add(a, b, expected):
    s = add(a, b)
    assert s == expected
