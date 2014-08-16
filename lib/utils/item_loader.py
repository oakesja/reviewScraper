class ItemLoader(object):
    def __init__(self, item):
        self._item = item

    def load_item(self):
        for attribute in self._item.attributes:
            attribute.load_value()