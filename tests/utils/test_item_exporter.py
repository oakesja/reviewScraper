import pytest

from lib.utils.item_exporter import ItemExporter
from lib.utils.exceptions import MyException


def test_export_full_item_json(item_with_one_value):
    e = ItemExporter(item_with_one_value, 'json')
    expected = '{"rating": "9.0", "site": "IGN"}'
    assert e.export() == expected


def test_export_item_with_empty_attrs_json(item_with_empty_attrs):
    e = ItemExporter(item_with_empty_attrs, 'json')
    expected = '{"rating": "9.0", "site": "IGN"}'
    assert e.export() == expected


def test_export_item_with_no_site_name_json(item_with_empty_site_name):
    e = ItemExporter(item_with_empty_site_name, 'json')
    expected = '{"rating": "9.0"}'
    assert e.export() == expected


def test_export_item_with_no_attrs_json(item_empty):
    e = ItemExporter(item_empty, 'json')
    expected = 'null'
    assert e.export() == expected


def test_export_full_item_dict(item_with_one_value):
    e = ItemExporter(item_with_one_value, 'dict')
    expected = {"rating": "9.0", "site": "IGN"}
    assert e.export() == expected


def test_export_item_with_empty_attrs_dict(item_with_empty_attrs):
    e = ItemExporter(item_with_empty_attrs, 'dict')
    expected = {"rating": "9.0", "site": "IGN"}
    assert e.export() == expected


def test_export_item_with_no_site_name_dict(item_with_empty_site_name):
    e = ItemExporter(item_with_empty_site_name, 'dict')
    expected = {"rating": "9.0"}
    assert e.export() == expected


def test_export_item_with_no_attrs_dict(item_empty):
    e = ItemExporter(item_empty, 'dict')
    expected = None
    assert e.export() == expected


def test_export_item_invalid_type(item_with_one_value):
    with pytest.raises(MyException):
        e = ItemExporter(item_with_one_value, '')
        e.export()