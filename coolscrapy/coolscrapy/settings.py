# -*- coding: utf-8 -*-

# Scrapy settings for coolscrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'coolscrapy'

SPIDER_MODULES = ['coolscrapy.spiders']
NEWSPIDER_MODULE = 'coolscrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'coolscrapy (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'coolscrapy.pipelines.ArticleDataBasePipeline': 5,
}

# linux pip install MySQL-python
DATABASE = {'drivername': 'mysql',
            'host': '127.0.0.1',
            'port': '3306',
            'username': 'root',
            'password': '8JhoTbTIiVngp3cNOkVp',
            'database': 'spider_test',
            'query': {'charset': 'utf8'}}