FROM python
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN mkdir /code
WORKDIR /code
RUN mkdir data
COPY data/ data/
COPY code/ .
ENTRYPOINT ["scrapy",  "crawl", "Dados_Abertos_CNPJ"]
