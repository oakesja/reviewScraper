from lxml import html


class IgnItemLoader(object):
    def __init__(self, item):
        self._item = item

    def get_attr_from_xpath(self, attribute_name, xpath, response):
        tree = html.fromstring(response.text)
        try:
            value = tree.xpath(xpath)
            value = default_formatter(value)
            setattr(self._item, attribute_name, value)
        except:
            return
    def get_item(self):
        return self._item


def default_formatter(value):
    return value[0].strip()
