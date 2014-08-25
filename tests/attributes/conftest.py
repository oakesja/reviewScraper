import pytest


@pytest.fixture(scope="session")
def valid_page():
    return '<!doctype html><html><div>test</div></html>'


@pytest.fixture(scope="session")
def valid_xpath():
    return '//div/text()'


@pytest.fixture(scope="session")
def invalid_xpath():
    return 'test'
