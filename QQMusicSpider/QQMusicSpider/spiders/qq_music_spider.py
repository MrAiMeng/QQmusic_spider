# -*- coding: utf-8 -*-
import scrapy

# 导入绝对路径下的item模块
from QQMusicSpider.items import QqmusicspiderItem

class QqMusicSpiderSpider(scrapy.Spider):
    name = '163_music_spider'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/#/discover/playlist']

    def parse(self, response):
        li_list = response.xpath('//ul[@id = "m-pl-container"]/li')
        for li in li_list:
            # 在使用item之前先利用导入的item模块实例化item
            item = QqmusicspiderItem()
            # 利用extract_first取第一个元素，若没有返回None，用extract取多个元素形成 列表
            item['title'] = li.xpath('./a/@title').extract_first()
            item['href'] = li.xpath('./a/@href').extract_first()
            item['img'] = li.xpath('./img/@src').extract_first()
            yield scrapy.Request(
                item['href'],
                # 此处callback为函数引用，后面接方法名
                callback = self.detail_url_parse,
                # 由于此处仅拿到部分数据，需将item传入详情页解析方法中
                meta = {'item': item}
            )
        next_url = response.xpath('//a[@text() = "下一页"]/@href').extract_first()
        if next_url != 'javascript:void(0)':
            next_url = 'https://music.163.com' + next_url
            yield scrapy.Request(
                next_url,
                # 由于下一页与首页解析方式相同，所以callback用相同方法
                callback = self.parse
            )

    def detail_url_parse(self,response):
        item = response.meta['item']
        li_list = response.xpath('//ul[@class = "f-hide"]/li')
        for li in li_list:
            item['song_name'] = li.xpath('./a/text()')
            item['song_href'] = 'https://music.163.com' + li.xpath('./a/@href')
        # 用yield将数据传入pipelines进行处理
        yield item