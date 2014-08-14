from lib.requesters.ignrequester import IgnRequester


def scrape(game_name):
    x = IgnRequester(game_name)
    x.scrape_item()
    return x.get_item_as_json()