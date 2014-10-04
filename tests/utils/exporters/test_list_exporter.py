import pytest

from lib.utils.exporters.list_exporter import ListExporter
from lib.utils.exceptions import MyException


def test_export_dict(item_list_attr):
    e = ListExporter(item_list_attr, 'dict')
    results = e.export()
    assert results[0] == {"gameName": "game1", "pictureLink": "link1"}
    assert results[1] == {"gameName": "game2", "pictureLink": "link2"}


def test_export_json(item_list_attr):
    e = ListExporter(item_list_attr, 'json')
    results = e.export()
    assert results == '[{"gameName": "game1", "pictureLink": "link1"}, {"gameName": "game2", "pictureLink": "link2"}]'


def test_export_item_invalid_type(item_list_attr):
    with pytest.raises(MyException):
        e = ListExporter(item_list_attr, '')
        e.export()