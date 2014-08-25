from mock import patch

from lib.attributes.xpath_attribute import XpathAttribute

@patch.object(XpathAttribute, 'get_page_text')
def test_load_value_valid(mock_get_page_text, valid_page, valid_xpath):
    mock_get_page_text.return_value = valid_page
    x = XpathAttribute(None, valid_page, valid_xpath)
    x.load_value()
    assert x.value == 'test'


@patch.object(XpathAttribute, 'format_value')
@patch.object(XpathAttribute, 'get_page_text')
def test_load_value_no_page_text(mock_get_page_text, mock_format_value):
    mock_get_page_text.return_value = None
    x = XpathAttribute('test', None, None)
    x.load_value()
    assert x.value is None
    assert not mock_format_value.called


@patch.object(XpathAttribute, 'format_value')
@patch.object(XpathAttribute, 'get_page_text')
def test_load_value_invalid_xpath(mock_get_page_text, mock_format_value, valid_page, invalid_xpath):
    mock_get_page_text.return_value = valid_page
    x = XpathAttribute(None, valid_page, invalid_xpath)
    x.load_value()
    assert x.value is None
    assert not mock_format_value.called

