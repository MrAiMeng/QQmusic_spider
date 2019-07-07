# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqmusicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 此处直接写item的键名等于scrapy.Field()不需添加init以及self
    title = scrapy.Field()
    img= scrapy.Field()
    href = scrapy.Field()
    song_name = scrapy.Field()
    song_href = scrapy.Field()