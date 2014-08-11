from lxml import html
import requests
from items.ignitem import IgnItem
from xpaths import ignxpaths

class IgnScraper(object):
	def __init__(self, game):
		game = game.replace(' ', '-')
		self._url = 'http://www.ign.com/games/' + game

	def scrape(self):
		page = requests.get(self._url)
		tree = html.fromstring(page.text)
		return tree.xpath(ignxpaths.rating)
