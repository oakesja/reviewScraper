import json

from lib.utils.exceptions import MyException


class ItemExporter(object):
    def __init__(self, item, export_type):
        self._item = item
        self._export_type = export_type

    def export(self):
        values = self._get_values()
        with_site = self._with_site_name(values)
        if self._export_type == 'json':
            return json.dumps(with_site)
        elif self._export_type == 'dict':
            return with_site
        else:
            raise MyException('Invalid export type')

    def _get_values(self):
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