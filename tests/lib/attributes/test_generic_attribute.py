from mock import Mock

from lib.attributes.generic_attribute import GenericAttribute


def test_get_page_text_200():
    page = Mock()
    page.status_code = 200
    page.text = 'test'
    attr = GenericAttribute('name', None, page)
    assert attr.get_page_text() == 'test'


def test_get_page_text_non_200():
    page = Mock()
    page.status_code = 404
    attr = GenericAttribute('name', None, page)
    assert attr.get_page_text() is None


def test_get_page_text_no_status_code():
    page = Mock()
    attr = GenericAttribute('name', None, page)
    assert attr.get_page_text() is None