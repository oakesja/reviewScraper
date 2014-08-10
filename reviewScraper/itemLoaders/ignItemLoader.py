from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose

class IgnItemLoader(ItemLoader):

    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(unicode.strip)

    # name_in = MapCompose(unicode.title)
    # name_out = Join()

    # price_in = MapCompose(unicode.strip)