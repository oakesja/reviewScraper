import requests
import logging

from lib.utils.item import Item
from lib.paths.ign_paths import *
from lib.utils.exporters.list_exporter import ListExporter

from lib.utils.formatters import all_text_from_html, find_search_key


class SearchScraper(object):
    def __init__(self, search_term):
        search_term = search_term.replace(' ', '%20').lower()
        self._url = "http://www.ign.com/search?q=" + search_term + "&page=0&count=10&filter=games&type=object&objectType=game"
        self._item = Item()
        self._logger = logging.getLogger(__name__)

    def scrape_results(self, export_type='json'):
        self._logger.info('Scraping search results from %s', self._url)
        response = requests.get(self._url)
        self._item.add_xpath_attribute(response, 'gameName', IgnSearchNameXpath(), lambda x: map(all_text_from_html, x))
        self._item.add_xpath_attribute(response, 'pictureLink', IgnSearchPictureLinkXpath(), lambda x: x)
        self._item.add_xpath_attribute(response, 'lookupKey', IgnSearchKeyXpath(), lambda x: map(find_search_key, x))
        self._item.add_xpath_attribute(response, 'platforms', IgnSearchPlatformsXpath(), lambda x: map(all_text_from_html, x))
        return self._item.export(export_type, ListExporter)
