import pytest

from lib.utils.exceptions import MyException


def test_export_json(item_with_one_value):
    expected = '{"rating": "9.0", "site": "IGN"}'
    assert item_with_one_value.export() == expected


def test_export_dictionary(item_with_one_value):
    expected = {"rating": "9.0", "site": "IGN"}
    assert item_with_one_value.export('dict') == expected


def test_export_invalid_type(item_with_one_value):
    with pytest.raises(MyException):
        item_with_one_value.export('')
