# -*- coding: utf-8 -*-
import scrapy


class CnpjSpider(scrapy.Spider):
    name = 'Dados_Abertos_CNPJ'
    allowed_domains = ['receita.economia.gov.br']
    start_urls = ['http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj']

    def parse(self, response):
        return {
            'last_update': response.css("#parent-fieldname-text span::text").extract_first(),
            'download_link' : response.css('a.external-link[title="Dados Abertos"]::attr(href)')\
                .extract_first()
            }
