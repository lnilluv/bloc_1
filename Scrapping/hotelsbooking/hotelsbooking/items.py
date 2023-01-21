# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelsbookingItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    hotel_name = scrapy.Field()
    hotel_url = scrapy.Field()
    hotel_score = scrapy.Field()
    hotel_description = scrapy.Field()


