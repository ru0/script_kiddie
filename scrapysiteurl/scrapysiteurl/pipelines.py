# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.exceptions import DropItem

from sqlalchemy.orm import sessionmaker
from models.db import Dy, db_connect, create_dy_table


class ScrapysiteurlPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    ''' write to file '''
    def __init__(self):
        self.file = open('items.jl', 'a')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    

class DuplicatesPipeline(object):
    """ Remove duplicate """
    def __init__(self):
        self.url_seen = set()

    def process_item(self, item, spider):
        if item['link'] in self.url_seen:
            raise DropItem("Duplicate item found!")
        elif item['link'].find('login.') != -1:
            raise DropItem("Drop the login page!")
        else:
            self.url_seen.add(item['link'])
        return item
    
    

class SavedyLinkPipeline(object):
    """docstring for ClassName"""
    def __init__(self):
        self.file = codecs.open('items.jl', 'wb',encoding='utf-8')

    def process_item(self, item, spider):
        """ deal with the par """
        if item:
            print item['name']
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("<Ruo> %s" % item)

    def spider_closed(self, spider):
        """ close the file """
        self.file.close()


class SaveToDatabasePipeline(object):
    
    def __init__(self):
        engine = db_connect()
        create_dy_table(engine)
        self.Session = sessionmaker(bind=engine)
  
    def process_item(self, item, spider):
        
        a = Dy(name = item['name'],
               link = item['download'])
        
        #print '<Ruo>'
        #print isinstance(item['name'],unicode)
        # encode unicode to gbk
        #print item['name'].encode('gbk')
        session = self.Session()
        #print a
        session.add(a)
        session.commit()
        return item
        
        
