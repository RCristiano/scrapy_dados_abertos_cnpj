# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request
import re
from threading import Thread


class DadosPublicosCnpjPipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open('data/last_update.json', 'r+')
        except:
            self.file = open('data/last_update.json', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        def down_files(link):
            urllib.request \
                .urlretrieve(link, 'data/{}' \
                .format(re.search('[^\/]+$', link).group()))

        try:
            archive = json.load(self.file)

            if item['last_update'] == archive['last_update']:
                return item
        except:
            pass

        data =  json.dumps(dict(item))
        self.file.truncate(0)
        self.file.seek(0)
        self.file.write(data)

        try:
            for link in item['download_links']:
                Thread(target=down_files, args=(link,)).start()
        except:
            pass

        return item
