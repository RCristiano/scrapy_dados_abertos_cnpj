Dados Abertos CNPJ
==================

Web Scraping Python with Scrapy framework

Download the CNPJ Open Data if it has been updated since the last download

[PT-BR] Realiza o download dos Dados Abertos de CNPJ se foram atualizados desde o último download

### Run it local
```sh
git clone https://github.com/RCristiano/scrapy_dados_abertos_cnpj.git
cd dados_publicos_cnpj/code
pip install -r requirements.txt
scrapy crawl Dados_Abertos_CNPJ
```
Info and files in code/data folder

### Run it with Docker-Compose
```sh
git clone https://github.com/RCristiano/scrapy_dados_abertos_cnpj.git
docker-compose up -d
```
Info and files in data folder

### The scraping URL
> http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj

### Framework
![Scrapy logo](https://scrapy.org/img/scrapylogo.png "Scrapy logo")
> https://scrapy.org/

### TODO
- [ ] Deploy with [Scrapyd](https://scrapyd.readthedocs.io/en/stable/)
- [ ] Schedule (quarterly)
- [ ] [Scrapy Cloud](https://scrapinghub.com/scrapy-cloud)