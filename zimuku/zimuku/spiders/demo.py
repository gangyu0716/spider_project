# -*- coding: utf-8 -*-
import scrapy

from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):
    name = "demo"

    allowed_domains = ["zimuku.net"]
    start_urls = ['http://zimuku.net/']

    def parse(self, response):
        moivename = response.xpath('//b/text()').extract()[0]

        items = {}
        items['第一个'] = moivename
        return items
