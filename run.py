import cherrypy
import os
import logging.config


from lib.scrapers.all_scraper import AllScraper
from lib.scrapers.ign_scraper import IgnScraper
from lib.scrapers.gamespot_scraper import GamespotScraper
from lib.utils.logger_settings import logger_settings


class Root(object):
    @cherrypy.expose
    def index(self):
        return '''<ul>
            <li>/reviews/all/&ltgame&gt</li>
            <li>/reviews/ign/&ltgame&gt</li>
            <li>/reviews/gamespot/&ltgame&gt</li>
            </ul>
            '''


class Review(object):
    @cherrypy.expose
    def all(self, game):
        return AllScraper(game).scrape()

    @cherrypy.expose
    def ign(self, game):
        return IgnScraper(game).scrape()

    @cherrypy.expose
    def gamespot(self, game):
        return GamespotScraper(game).scrape()

if __name__ == '__main__':
    logging.config.dictConfig(logger_settings())
    root = Root()
    root.reviews = Review()
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
    cherrypy.quickstart(root)


