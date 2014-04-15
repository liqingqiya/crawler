#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

from scrapy.selector import Selector
from scrapy.spider import Spider
from musics.items import MusicsItem

class MusicsSpider(Spider):
    name = "musics"
    start_urls = ["http://music.baidu.com"]

#解析函数命名一定要是parse()
    def parse(self, response):
      sel = Selector(response)
      items = []
      sites = sel.xpath('//ul[@class="song-list"]/li')
      for site in sites:
        item = MusicsItem()
        item['song_name'] = site.xpath('span[@class="song-name"]/a/text()').extract()
        item['author_name'] = site.xpath('span[@class="singer-name"]/span[@class="author_list"]/@title').extract()
        items.append(item)
      return items
