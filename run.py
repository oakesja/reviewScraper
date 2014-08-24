import cherrypy
import os

from lib.scrapers.ign_scraper import IgnScraper


#TODO add lettuce/behave test for integration testing
class Root(object):
    @cherrypy.expose
    def index(self):
        return "Usage:"

    @cherrypy.expose
    def reviews(self, game):
        scraper = IgnScraper(game)
        return scraper.scrape()

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000'))})
    cherrypy.quickstart(Root())


