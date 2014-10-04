import lxml
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


def test_take_all_comma_normal():
    assert take_all_comma([' x ', ' y ']) == 'x, y'


def test_take_all_comma_empty_strings():
    assert take_all(['', 'x']) is 'x'


def test_take_all_comma_empty():
    assert take_all_comma([]) is None


def test_take_all_comma_non_string():
    assert take_all_comma([9, 1]) is None


def test_take_all_comma_non_list():
    assert take_all_comma(9) is None
    assert take_all_comma(None) is None


def test_take_all_normal():
    assert take_all([' x ', ' y ']) == 'x y'


def test_take_all_empty_strings():
    assert take_all(['', 'x']) is 'x'


def test_take_all_empty():
    assert take_all([]) is None


def test_take_all_non_string():
    assert take_all([9, 1]) is None


def test_take_all_non_list():
    assert take_all(9) is None
    assert take_all(None) is None


def test_take_all_text():
    html = lxml.html.fromstring('<div><a>test</a> all </div>')
    assert all_text_from_html(html) == 'test all'


def test_take_all_text_non_string():
    assert all_text_from_html(9) is None


def test_find_search_key():
    assert find_search_key("http://www.ign.com/games/fallout/mac-3512") == "fallout"