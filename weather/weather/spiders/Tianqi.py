# -*- coding: utf-8 -*-
import scrapy

from weather.items import WeatherItem

class TianqiSpider(scrapy.Spider):
    name = "Tianqi"
    allowed_domains = ["https://www.tianqi.com/nanjing/"]
    start_urls = ['https://www.tianqi.com/nanjing/']

    def parse(self, response):
        # 解析数据

        items = []

        # 从《week》属性中爬取一周的日期，星期，和天气图标
        week = response.xpath('//ul[@class="week"]').xpath('./li')
        # 从《txt txt2》属性中爬取一周的天气
        weather = response.xpath('//ul[@class="txt txt2"]').xpath('./li')
        # 从《txt》属性中爬取一周的风向
        wind = response.xpath('//ul[@class="txt"]').xpath('./li')
        # 从《zxt_shuju》属性中爬取一周的温度数据
        temperature = response.xpath('//div[@class="zxt_shuju"]').xpath('./ul/li')
        # 爬取每天的信息
        for i in range(6):
            weekitem = WeatherItem()
            weekitem['date'] = week[i].xpath('./b/text()').extract()[0]
            weekitem['week'] = week[i].xpath('./span/text()').extract()[0]
            weekitem['img'] = week[i].xpath('./img/@src').extract()[0]

            weekitem['weather'] = weather[i].xpath('./text()').extract()[0]

            weekitem['wind'] = wind[i].xpath('./text()').extract()[0]

            weekitem['temperature'] = temperature[i].xpath('./b/text()').extract()[0] + \
                ' ~ ' + \
                temperature[i].xpath('./span/text()').extract()[0]

            items.append(weekitem)
        return items
