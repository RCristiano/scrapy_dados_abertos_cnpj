# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import urllib.request


class DadosPublicosCnpjPipeline(object):
    def open_spider(self, spider):
        try:
            self.file = open('data/last_update.json', 'r+')
        except:
            self.file = open('data/last_update.json', 'w+')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        try:
            archive = json.load(self.file)

            if item['last_update'] == archive['last_update']:
                return item
        except:
            pass

        line =  json.dumps(dict(item))
        self.file.truncate(0)
        self.file.seek(0)
        self.file.write(line)

        urllib.request\
            .urlretrieve(item['download_link'],
                        'data/DADOS_ABERTOS_CNPJ.zip')

        return item
