# -*- coding: utf-8 -*-

import scrapy
import math

class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-hyperlink h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            'votes': response.css('.question .vote-count-post::text').extract()[0],
            'body': response.css('.question .post-text').extract()[0],
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
    

#
#如果一个函数包含yield关键字，这个函数就会变为一个生成器。
#生成器并不会一次返回所有结果，而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。

# 通过`yield`来创建生成器
def func():
    for i in xrange(10):
        yield i

# 通过列表来创建生成器
[i for i in xrange(10)]

f = func()

print f.next


#生成一个满足要求的很大的列表

'''
def get_primes(num):
    while True:
        if (num % 2) == 0:
            yield num
        num += 1
        
f = get_primes(2)
>>> f.next()
2
'''


strurl = "//www.baidu.com"

print strurl[2:]



