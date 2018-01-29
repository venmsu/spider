# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianmaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GOODS_PRICE = scrapy.Field()  # 价格
    GOODS_NAME = scrapy.Field()  # 名称
    GOODS_URL = scrapy.Field()  # 商店链接
    SHOP_NAME = scrapy.Field()  # 商店名称
    SHOP_URL = scrapy.Field()  # 商店链接
