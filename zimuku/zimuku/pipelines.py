# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZimukuPipeline(object):
    def process_item(self, item, spider):
        #print ('1111111111')
        print (item)
        return item
