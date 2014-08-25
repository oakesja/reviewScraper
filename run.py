import cherrypy
import os
import logging

from lib.scrapers.all_scraper import AllScraper
from lib.scrapers.ign_scraper import IgnScraper
from lib.scrapers.gamespot_scraper import GamespotScraper


class Root(object):
    @cherrypy.expose
    def index(self):
        return '''<ul>
            <li>/review/all/&ltgame&gt</li>
            <li>/review/ign/&ltgame&gt</li>
            <li>/review/gamespot/&ltgame&gt</li>
            </ul>
            '''


class Review(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def all(self, game):
        return AllScraper(game).scrape()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def ign(self, game):
        return IgnScraper(game).scrape()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def gamespot(self, game):
        return GamespotScraper(game).scrape()

if __name__ == '__main__':
    logging.basicConfig(filename='review_scraper.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    root = Root()
    root.reviews = Review()
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
    cherrypy.quickstart(root)


