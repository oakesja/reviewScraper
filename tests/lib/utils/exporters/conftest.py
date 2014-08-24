import pytest

from lib.attributes.xpath_attribute import XpathAttribute
from lib.utils.item import Item


@pytest.fixture(scope="session")
def item_with_one_value():
    item = Item('ign')
    item.attributes.append(XpathAttribute('rating', None, None, None, '9.0'))
    return item


@pytest.fixture(scope="session")
def item_with_empty_attrs():
    item = Item('ign')
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
    item = Item('ign')
    return item