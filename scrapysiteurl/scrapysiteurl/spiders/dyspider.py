# -*- coding: utf-8 -*-
import scrapy
from scrapysiteurl.items import DyItem,DydownloadItem

class DyspiderSpider(scrapy.Spider):
    name = "dyspider"
    #allowed_domains = ["dy2018.com"]
    start_urls = ['http://www.dy2018.com/4/']

    def parse(self, response):
        '''
        with open('cache.tmp', 'wb') as f:
            f.write(response.body)
        '''
        self.log('A response from %s just arrived!' % response.url)
        
        for sel in response.xpath('//table[@class="tbspan"]//tr[2]//a[2]'):
            item = DyItem()
            item['name'] = sel.xpath('@title').extract_first()
            item['link'] = sel.xpath('@href').extract_first()
            # has a bug
            yield scrapy.Request(response.urljoin(item['link']), meta={'item': item}, callback = self.parse_download)
        
        next_page = response.xpath('//a[contains(.,"下一页")]/@href'.decode('utf-8')).extract_first()
        #next_page = response.xpath('(//div[@class="x"])[2]//a[1]/@href').extract()[0]
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
    
    def parse_download(self,response):
        # meta传递了item
        download = []
        item = response.meta['item']
        dlitem = DydownloadItem()
        dlitem['name'] = item['name']
        for dlink in response.xpath('//td[@bgcolor="#fdfddf"]//a/@href').extract():
            download.append(dlink)
        # download list
        dlitem['download'] = ','.join(download)
        # return multiple parameters
        yield dlitem
