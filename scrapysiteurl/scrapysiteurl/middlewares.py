# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class RandomUserAgentMiddleware(UserAgentMiddleware):
    """ override the default user agent """
    
    def __init__(self, settings, user_agent = ''):
        super(RandomUserAgentMiddleware, self).__init__()
        # must set the default user_agent to null
        self.user_agent = user_agent
        user_agent_list_file = settings.get('USER_AGENT_FILE')
        with open(user_agent_list_file, 'r') as f:
            self.user_agent_list = [line.strip()[1:-1] for line in f.readlines()]

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler.settings)
        crawler.signals.connect(obj.spider_opened,
                                signal=signals.spider_opened)
        return obj

    def process_request(self, request, spider):
        self.user_agent = random.choice(self.user_agent_list)
        if self.user_agent:
            request.headers.setdefault('User-Agent', self.user_agent)
