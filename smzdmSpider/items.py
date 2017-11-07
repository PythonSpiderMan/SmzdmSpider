# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HotSearchItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()


class Tags(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()


class SmzdmspiderItem(HotSearchItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
