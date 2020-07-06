from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError
import csv

def ProcurarPaginasLivros(new_url, qnt_de_paginas=50):
    # Inicializando o Chromium:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    lista_pagina_de_livro = []

    # Loop de 50 paginas:
    for i in range(1, qnt_de_paginas+1):
        # Cria a Url para extrair os 20 livros
        new_url = new_url[:new_url.find('-')+1]+str(i)+'.html'

    # Carregando a pagina:
        driver.get(new_url)

        page_html = driver.page_source
        page_soup = soup(page_html, "html.parser")

        # Encontra todas as molduras dos livros na pagina:
        containers = page_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

        # Repetição para cada livro na pagina (20 repetições):
        for container in containers:
            # Obtêm a pagina especifica do livro:
            pagina_livro = container.article.h3.a["href"]

            # Adiciona a informação em uma lista
            lista_pagina_de_livro.append(pagina_livro)

    driver.close()
    return lista_pagina_de_livro

def CrawlInfoLivros(lista_pagina_de_livro, url):
    # Inicializando o Chromium:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    biblioteca = []

    # Acessa cada pagina especifica do livro:
    for sub_domain in lista_pagina_de_livro:

        # Acessando a pagina especifica e baixando as informaçãoes:
        driver.get(url + 'catalogue/' + sub_domain)
        page_html = driver.page_source
        page_soup = soup(page_html, "html.parser")

        # OBTENÇÃO DAS INFORMAÇÕES:
        # Titulo do Livro:
        livro_nome = page_soup.find("div", {"class": "col-sm-6 product_main"}).h1.text

        # Genero do Livro:
        livro_genero = page_soup.findAll("ul", {"class": "breadcrumb"})[0].select_one("li:nth-of-type(3)").a.text

        # Preço do Livro:
        livro_preco = page_soup.find("p", {"class": "price_color"}).text.strip()[1:]

        # Taxa do Livro:
        livro_taxa = page_soup.find("tbody").select_one("tr:nth-of-type(5)").td.text.strip()[1:]

        # Quantidade de estrelas:
        livro_estrela = page_soup.find("div", {"class": "col-sm-6 product_main"}).select_one("p:nth-of-type(3)")['class'][1]

        # Número de Reviews:
        livro_reviews = page_soup.find("tbody").select_one("tr:nth-of-type(7)").td.text

        # Estoque dos livros
        estoque = page_soup.find("p", {"class": "instock availability"}).text.strip()
        # livro_disponibilidade = estoque[:estoque.find('(')-1]
        livro_estoque = estoque[estoque.find('(')+1:].split()[0]

        # UPC do Livro:
        livro_UPC = page_soup.find("tbody").tr.td.text

        livro_info = [livro_nome, livro_genero,livro_preco, livro_taxa, livro_estrela, livro_reviews, livro_estoque, livro_UPC]
        biblioteca.append(livro_info)
    # Fecha o Chromium:
    driver.close()
    return biblioteca

def SalvarEmCsv(biblioteca):
    # Salvando em um documento .csv:
    with open('books_scrap.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)

        # Linha para os titulos:
        thewriter.writerow(['Titulo', 'Genero', 'Preco', 'Taxa', 'Estrelas', 'Reviews', 'Estoque', 'UPC'])

        # Entradas dos livros:
        for livro in biblioteca:
            thewriter.writerow(livro)