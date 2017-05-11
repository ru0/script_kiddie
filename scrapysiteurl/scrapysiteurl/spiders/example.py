# -*- coding: utf-8 -*-
import scrapy
from scrapysiteurl.items import SiteurlItem

class ExampleSpider(scrapy.Spider):
    name = "scrapysiteurl"
    allowed_domains = ["domain.com"]
    start_urls = ['https://www.domain.com/']

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        for sel in response.xpath('//a[@href]'): # 选择所有包含href属性的a标签
            item = SiteurlItem()
            link = str(sel.re('href="(.*?)"')[0])
            item['link'] = link
            url = response.urljoin(item['link'])
            yield scrapy.Request(url, callback=self.parse_more)
            
    def parse_more(self,response):
        for sel in response.xpath('//a[@href]'):
            item = SiteurlItem()
            link = str(sel.re('href="(.*?)"')[0])
            item['link'] = link
            yield item
            
        
