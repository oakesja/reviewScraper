class ItemLoader(object):
    def __init__(self, item):
        self._item = item

    # TODO add a test
    def load_item(self):
        for attribute in self._item.attributes:
            attribute.load_value()