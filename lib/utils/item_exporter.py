import json
import logging

from lib.utils.exceptions import MyException


class ItemExporter(object):
    def __init__(self, item, export_type):
        self._item = item
        self._export_type = export_type
        self._logger = logging.getLogger(__name__)

    def export(self):
        values = self._get_values()
        with_site = self._with_site_name(values)
        if self._export_type == 'json':
            return json.dumps(with_site)
        elif self._export_type == 'dict':
            return with_site
        else:
            self._logger.error("Invalid export type %s", self._export_type)
            raise MyException('Invalid export type')

    def _get_values(self):
        values = dict()
        for attr in self._item.attributes:
            if attr.value:
                values[attr.name] = attr.value
        return values

    def _with_site_name(self, values):
        if self._item.site_name and values:
            values["site"] = self._item.site_name
            return values
        if self._item.site_name:
            self._logger.info("No values found to export")
            return None
        else:
            return values