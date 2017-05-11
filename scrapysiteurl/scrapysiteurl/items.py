# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapysiteurlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SiteurlItem(scrapy.Item):
    """ get page url item """
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    
class DyItem(scrapy.Item):
    """ main page item """
    name  = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class DydownloadItem(scrapy.Item):
    """ download page item """
    name  = scrapy.Field()
    download = scrapy.Field()


# TEST
#url = SiteurlItem(link='www.baidu.com',title='baidu')
#print url
#print url['link']
#dic
#for key,value  in url.items():
#    print key,value
    
#item = SiteurlItem()
#item['title'] = 'title1'
#print item['title']

#title = []

#title.append('1')
#title.append('2')

#print title

#item['title'] = title
#print type(item['title'])
#print  ','.join(item['title'])

#print ','.join(['1'])