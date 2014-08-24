from lib.utils.formatters import *


def test_take_first_normal():
    assert take_first(['    9    ']) == '9'


def test_take_first_empty():
    assert take_first([]) is None


def test_take_first_non_string():
    assert take_first([9]) is None


def test_take_first_non_list():
    assert take_first(9) is None
    assert take_first(None) is None