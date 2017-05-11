#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from coolscrapy.items import HuxiuItem
import scrapy

class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/"
    ]

    def parse(self, response):
        # //div[@class="mine"]: 选择所有包含 class="mine" 属性的div 标签元素
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            item = HuxiuItem()
            # 初始化一个字典对象
            item['title'] = sel.xpath('h2/a/text()')[0].extract()
            item['link'] = sel.xpath('h2/a/@href')[0].extract()
            url = response.urljoin(item['link'])
            #print(item['title'],item['link'])
            # 继续跟踪每个链接进去
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        detail = response.xpath('//div[@class="article-wrap"]')
        item = HuxiuItem()
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['link'] = response.url
        print(item['title'],item['link'])
        yield item