# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "dy2018"
    allowed_domains = ["dy2018.com"]
    start_urls = ['http://www.dy2018.com/4/']

    def parse(self, response):
        #//table[@class="tbspan"]//tr[2]//a[@class="ulink"]
        for sel in response.xpath('//table[@class="tbspan"]//tr[2]'):
            title = sel.xpath('a[2]/text()').extract()
            
