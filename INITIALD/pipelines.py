# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

import pymysql
pymysql.install_as_MySQLdb()

import MySQLdb.cursors
from twisted.enterprise import adbapi
from INITIALD.items import ForumItem

class InitialdPipeline(object):

    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparms=dict(
            host=settings["MYSQL_HOST"],
            user = settings["MYSQL_USER"],
            password = settings["MYSQL_PASSWD"],
            database = settings["MYSQL_DBNAME"],
            port = settings["MYSQL_PORT"],
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
            charset = "utf8",
        )
        dbpool=adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self,item,spider):
        query=self.dbpool.runInteraction(self.insert,item)#调用插入的方法
        query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item

    def insert(self,tx,item):
        if isinstance(item,ForumItem):
            sql="insert into forum_info(url,title,img,keyword) values(%s,%s,%s,%s)"
            params=(item["url"],item["title"],item["img"],item["keyword"])
            tx.execute(sql,params)
            print('---------------------------------插入成功')

    def _handle_error(self, failue, item, spider):
        print(failue)
