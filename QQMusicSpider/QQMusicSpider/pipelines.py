# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import mongo_client

class QqmusicspiderPipeline(object):
    def process_item(self, item, spider):
        # 创建mongdb数据库储存数据
        client = mongo_client()
        collection = client['163music']['songs']
        collection.insert(item)
        return item
