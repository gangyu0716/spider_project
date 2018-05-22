# -*- coding: utf-8 -*-
import scrapy

from weather.items import WeatherItem

class TianqiSpider(scrapy.Spider):
    name = "Tianqi"
    allowed_domains = ["https://www.tianqi.com/nanjing/"]
    start_urls = ['https://www.tianqi.com/nanjing/']

    weeks = []

    def parse(self, response):
        #解析数据

        weekitem = WeatherItem()
        #从week属性中爬去日期，星期，和天气图标
        day7 = response.xpath('//ul[@class="week"]').xpath('./li')
        for day in day7:
            weekitem['data'] = day.xpath('./b/text()').extract()[0]
            weekitem['week'] = day.xpath('./span/text()').extract()[0]
            weekitem['img'] = day.xpath('./img/@src').extract()[0]

        day7 = response.xpath('//ul[@class="txt txt2"]').xpath('./li')
        for day in day7:
            weekitem['weather'] = day.xpath('')
        print (weekitem['img'])
        return weekitem