# -*- coding: utf-8 -*-

import scrapy


class CnpjSpider(scrapy.Spider):
    name = 'Dados_Abertos_CNPJ'
    allowed_domains = ['receita.economia.gov.br']
    start_urls = ['http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj']

    def parse(self, response):
        d = {}

        d['last_update'] = response.css("#parent-fieldname-text p::text").re(r'Data.*\d')[0]

        for i, r in enumerate(response.css('a.external-link::attr(href)').re(r'http.+/DADOS_ABERTOS_CNPJ_\d+\.zip')):
            d['file_{}'.format(i)] = r

        return d

        # return {
        #     'last_update': response.css("#parent-fieldname-text p::text").extract_first(),
        #     'download_link' : response.css('a.external-link[title="Dados Abertos"]::attr(href)')\
        #         .extract_first()
        #     }
