from lib.utils.exporters.json_item_exporter import JsonItemExporter


def test_export_full_item(item_with_one_value):
    j = JsonItemExporter(item_with_one_value)
    expected = '{"ign": {"rating": "9.0"}}'
    assert j.export() == expected


def test_export_item_with_empty_attrs(item_with_empty_attrs):
    j = JsonItemExporter(item_with_empty_attrs)
    expected = '{"ign": {"rating": "9.0"}}'
    assert j.export() == expected


def test_export_item_with_no_site_name(item_with_empty_site_name):
    j = JsonItemExporter(item_with_empty_site_name)
    expected = '{"rating": "9.0"}'
    assert j.export() == expected


def test_export_item_with_no_attrs(item_empty):
    j = JsonItemExporter(item_empty)
    expected = '{"ign": null}'
    assert j.export() == expected