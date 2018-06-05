# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import requests
#import json
#import codecs
#import pymysql

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 获取爬虫路径，设置数据保存文件的位置
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.txt'
        print (type(item))
        print (item)

        print (base_dir)
        if os.path.exists(base_dir + '/data'):
            print('path exist')
        else:
            os.mkdir(base_dir + '/data')
            print("create path -- " + base_dir + '/data')

        # 将数据写入文件
        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n')
            f.write(item['temperature'] + '\n')

        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item
