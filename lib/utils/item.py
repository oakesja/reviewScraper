from lib.attributes.xpath_attribute import XpathAttribute
from lib.utils.exporters.json_item_exporter import JsonItemExporter
from lib.utils.formatters import take_first


class Item(object):
    def __init__(self, site_name):
        self._attributes = []
        self._site_name = site_name

    @property
    def attributes(self):
        return self._attributes

    @property
    def site_name(self):
        return self._site_name

    def add_xpath_attribute(self, page, name, xpath, formatting_method=take_first):
        attr = XpathAttribute(name, page, xpath, formatting_method)
        self._attributes.append(attr)

    def export(self):
        self.load_item()
        return JsonItemExporter(self).export()

    def load_item(self):
        for attribute in self._attributes:
            attribute.load_value()

