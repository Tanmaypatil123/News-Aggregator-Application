# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
import scrapy
from main.models import News_data


class NewsSpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    heading = scrapy.Field()
    img = scrapy.Field()
    url = scrapy.Field()

