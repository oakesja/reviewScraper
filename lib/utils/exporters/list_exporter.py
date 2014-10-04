import json
import logging

from lib.utils.exceptions import MyException


class ListExporter(object):
    def __init__(self, item, export_type):
        self._item = item
        self._export_type = export_type
        self._logger = logging.getLogger(__name__)

    def export(self):
        results = self._get_results()
        if self._export_type == 'dict':
            return results
        elif self._export_type == 'json':
            return json.dumps(results)
        else:
            self._logger.error("Invalid export type %s", self._export_type)
            raise MyException('Invalid export type')

    def _get_results(self):
        results = list()
        for k in range(len(self._item.attributes[0].value)):
            results.append(dict())
        for attr in self._item.attributes:
            for i in range(len(attr.value)):
                results[i][attr.name] = attr.value[i]
        return results