from lib.requesters.ignrequester import IgnRequester


def scrape(game_name):
    x = IgnRequester(game_name)
    x.scrape_item()
    print x.get_item_as_json()