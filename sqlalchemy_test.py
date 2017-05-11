#/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


print(sqlalchemy.__version__)

engine = create_engine('sqlite:///foo.db',echo=True)

Base = declarative_base()

class News(Base):
    ''' 创建表对象'''
    __tablename__ = 'news'
    id = Column(Integer,primary_key=True)
    title = Column(String)
    url = Column(String)
    
    def __repr__(self):
        return "<News(title = '%s',url = '%s')>" % (self.title,self.url)

# 创建数据库
#Base.metadata.create_all(engine)

ed_news = News(title = 'biaoti',url='www.baidu.com')
print ed_news

# 插入数据库
Session = sessionmaker(bind=engine)
session = Session()  # 先使用工程类来创建一个session
session.add(ed_news)


# 同时创建多个
'''
session.add_all([
    News(title='wendy', url='Wendy Williams'),
    News(title='mary', url='Mary Contrary'),
    News(title='fred', url='Fred Flinstone')])
'''

# 查询语句
#our_news = session.query(News).filter_by(id = 1).first()

for i in session.query(News).order_by(News.id):
    print(i.title, i.url)


# 提交事务
session.commit()

