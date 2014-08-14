from lib import scraper
import cherrypy


class Root(object):
    @cherrypy.expose
    def index(self):
        return "Usage:"

    @cherrypy.expose
    def reviews(self, game):
        print game
        ret = scraper.scrape(game)
        return ret

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')


