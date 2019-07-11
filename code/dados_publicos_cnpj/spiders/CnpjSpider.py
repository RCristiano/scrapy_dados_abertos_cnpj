# -*- coding: utf-8 -*-

import scrapy


class CnpjSpider(scrapy.Spider):
    name = 'Dados_Abertos_CNPJ'
    allowed_domains = ['receita.economia.gov.br']
    start_urls = [
        'http://receita.economia.gov.br/orientacao/tributaria/cadastros/'
        + 'cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj']

    def parse(self, response):
        d = {}

        d['last_update'] = response.css("#parent-fieldname-text p::text") \
            .re(r'Data.*\d')[0]

        d['download_links'] = []

        for r in response.css('a.external-link::attr(href)') \
            .re(r'http.+/DADOS_ABERTOS_CNPJ_\d+\.zip'):
            d['download_links'].append(r)

        return d
