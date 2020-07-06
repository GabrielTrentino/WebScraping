import schedule
import time
import books_spider

def WebCrawl():
    new_url = 'http://books.toscrape.com/catalogue/page-1.html'
    lista_pagina_de_livro = books_spider.ProcurarPaginasLivros(new_url)

    url = 'http://books.toscrape.com/'
    biblioteca = books_spider.CrawlInfoLivros(lista_pagina_de_livro, url)
    books_spider.SalvarEmCsv(biblioteca)

schedule.every(1).day.at("08:00").do(WebCrawl)

while 1:
    schedule.run_pending()
    time.sleep(60)