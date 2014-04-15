#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado
import logging
import json

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("begin...")

file = open("musics.json","r").read()
file = json.loads(file)
for line in file:
  try:
    print "sone-name:\t%s\t\t\tauthor:\t%s"%(line["song_name"][0],line["author_name"][0])
  except IndexError: 
    print "sone-name:\t%s\t\t\tauthor:\t%s"%(line["song_name"][0],"someone")
    continue
logger.info("end...")

