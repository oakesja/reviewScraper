import logging

from lib.utils.formatters import take_first


class GenericAttribute(object):
    def __init__(self, name, value, page, formatting_method=take_first):
        self._name = name
        self._value = value
        self._page = page
        self._formatting_method = formatting_method
        self._logger = logging.getLogger(__name__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @property
    def formatting_method(self):
        return self._formatting_method

    @formatting_method.setter
    def formatting_method(self, x):
        self._formatting_method = x

    def format_value(self):
        self._value = self._formatting_method(self._value)

    def get_page_text(self):
        if self._page.status_code == 200:
            return self._page.text
        else:
            self._logger.info("Getting page failed with status code %s", self._page.status_code)
            return None
