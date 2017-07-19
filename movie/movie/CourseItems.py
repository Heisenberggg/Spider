import scrapy

class Courseitem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    introduction = scrapy.Field()
    score = scrapy.Field()
    image_url = scrapy.Field()
    image_path = scrapy.Field()