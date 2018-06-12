# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import requests
import json
import codecs
import pymysql

# process

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 获取爬虫路径，设置数据保存文件的位置
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.txt'
        # print (type(item))
        # print (item)

        # print (base_dir)
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
            f.write('\r\n')

        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item


class W2json(object):
    def process_item(self,item,spider):
        base_dir = os.getcwd()
        filename = base_dir + '/data/weather.json'

        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item

class W2mysql(object):
    def process_item(self,item,spider):

        date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']
        img = item['img']

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='gy000940',
            db='scrapyDB',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = """INSERT INTO weather(date,week,temperature,weather,wind,img)
                        VALUES (%s, %s,%s,%s,%s,%s)"""
                cursor.execute(
                    sql, (date, week, temperature, weather, wind, img))

            connection.commit()

        finally:
            connection.close()

        return item