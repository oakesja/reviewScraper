from lxml import html
import logging

from lib.utils.formatters import take_first
from generic_attribute import GenericAttribute


class XpathAttribute(GenericAttribute):
    def __init__(self, name, page, xpath, formatting_method=take_first, value=None):
        super(XpathAttribute, self).__init__(name, value, page, formatting_method)
        self._xpath = xpath
        self._logger = logging.getLogger(__name__)

    @property
    def xpath(self):
        return self._xpath

    @xpath.setter
    def xpath(self, value):
        self._xpath = value

    def load_value(self):
        page_text = self.get_page_text()
        self._parse_page_text(page_text)

    def _parse_page_text(self, page_text):
        if page_text:
            tree = html.fromstring(page_text)
            self._value = tree.xpath(self._xpath)
            self._format_value()
        else:
            self._value = None

    def _format_value(self):
        if self._value:
            self._logger.info('Xpath to %s attribute succeeded', self._name)
            self.format_value()
        else:
            self._logger.info('Xpath to %s attribute failed', self._name)
            self._value = None