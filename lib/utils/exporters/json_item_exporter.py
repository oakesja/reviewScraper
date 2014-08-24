import json


class JsonItemExporter(object):
    def __init__(self, item):
        self._item = item

    def export(self):
        json_values = self._get_values_json()
        json_all = self._with_site_name(json_values)
        return json.dumps(json_all)

    def _get_values_json(self):
        values = dict()
        for attr in self._item.attributes:
            if attr.value:
                values[attr.name] = attr.value
        return values

    def _with_site_name(self, values):
        site = dict()
        if self._item.site_name and values:
            site[self._item.site_name] = values
            return site
        if self._item.site_name:
            site[self._item.site_name] = None
            return site
        else:
            return values