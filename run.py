from lib.scrapers.ign_scraper import IgnScraper
import cherrypy


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
    cherrypy.config.update({'server.socket_port': 5000})
    cherrypy.quickstart(Root(), '/')


