# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZimukuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def process_item(self, item, spider):
        print (item)
        return item
    pass
