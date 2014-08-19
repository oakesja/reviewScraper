import json


class JsonItemExporter(object):
    def __init__(self, item):
        self._item = item

    # TODO add a test
    def export(self):
        values = dict()
        for attr in self._item.attributes:
            values[attr.name] = attr.value
        site = dict()
        site[self._item.site_name] = values
        return json.dumps(site)