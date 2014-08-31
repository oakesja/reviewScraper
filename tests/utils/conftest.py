import pytest
from mock import Mock

from lib.attributes.xpath_attribute import XpathAttribute
from lib.utils.item import Item
from lib.utils.formatters import take_first


@pytest.fixture(scope="session")
def item_with_one_value():
    page = Mock
    page.status_code = 200
    page.text = '<div>9.0</div>'
    xpath = '//div/text()'
    item = Item('IGN')
    item.attributes.append(XpathAttribute('rating', page, xpath, take_first, '9.0'))
    return item


@pytest.fixture(scope="session")
def item_with_empty_attrs():
    item = Item('IGN')
    item.attributes.append(XpathAttribute('rating', None, None, None, '9.0'))
    item.attributes.append(XpathAttribute('description', None, None, None, None))
    return item


@pytest.fixture(scope="session")
def item_with_empty_site_name():
    item = Item(None)
    item.attributes.append(XpathAttribute('rating', None, None, None, '9.0'))
    return item


@pytest.fixture(scope="session")
def item_empty():
    item = Item('IGN')
    return item