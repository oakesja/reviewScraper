from generic_attribute import GenericAttribute
from lxml import html

class XpathAttribute(GenericAttribute):
    def __init__(self, name, page, xpath, formatting_method, value=None):
        super(XpathAttribute, self).__init__(name, value, page, formatting_method)
        self._xpath = xpath

    @property
    def xpath(self):
        return self._xpath

    @xpath.setter
    def xpath(self, value):
        self._xpath = value

    @xpath.deleter
    def xpath(self):
        del self._xpath

    # TODO add tests for
    def load_value(self):
        tree = html.fromstring(self._page.text)
        self._value = tree.xpath(self._xpath)
        super(XpathAttribute, self).format_value()