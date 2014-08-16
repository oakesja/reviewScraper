from lib.scrapers.ign_scraper import IgnScraper
import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self):
        return "Usage:"

    @cherrypy.expose
    def reviews(self, game):
        scraper = IgnScraper(game)
        return scraper.scrape()

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')


