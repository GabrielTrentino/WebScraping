![](https://github.com/GabrielTrentino/WebScraping/blob/master/00-img/01-BooksToScrape.png?raw=true)
# Book to Scrape
[Books to Scrape](http://books.toscrape.com/) é um site criado com a **unica finalidade de praticar o *Web Scraping*** e, a partir desse site, o [Meigarom](https://www.youtube.com/channel/UCar5Cr-pVz08GY_6I3RX9bA) a elaboração de um Projeto de Data Engineering em seu [post](https://sejaumdatascientist.com/o-projeto-de-data-engineering-para-o-seu-portfolio/) na qual foi inspiração para realizar este projeto. A Situação Ficticia foi sintetizada com minhas palavras de acordo com a ideia geral passada no post.

Situação Ficticia: Uma Startup de troca de livros possui um modelo de negócio à base na troca de livros cadastrados pelo usuário. O objetivo como Data Scientist é de construir um **Sistema de Recomendação de Compra** de livros melhores avaliados por gênero. Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

1. O **nome** do livro;
2. A **categoria** do livro;
3. O **número de estrelas** que o livro recebeu;
4. O **preço** do livro;
5. Se o livro **está em Estoque ou não**.

## COMO FOI REALIZADA:

*  O Web Scrapper foi realizado utilizando a linguagem Python;
    * Foram utilizados: `Selenium` e `BeautifulSoup`;
    * Modularização das Funções;
* **(PRECISA SER FEITO)** Configurar o banco de dado Postgres;
    * **(PRECISA SER FEITO)** Sincronizar os scripts de Python com o banco de dados Postgres;
    * **(PRECISA SER FEITO)** Um Script so pode rodar quando outro terminar;
* Foi criado um arquivo [`.csv`](https://github.com/GabrielTrentino/WebScraping/blob/master/01-BooksToScrape/books_scrap.csv) com o Python;
* Agendar o script para rodar em horários específicos;
* **(PRECISA SER FEITO)** Garantir que o script saiba lidar com problemas (internet lenta, página não encontrada, objeto não carregado, etc);
* [Análise Exploratória](https://github.com/GabrielTrentino/WebScraping/blob/master/01-BooksToScrape/Books_To_Scrape.ipynb) dos Dados extraídos;
    * Recomendar os livros com maior avaliação entre os gêneros;
    
## TOMADAS DE DECISÃO:

A Análise Exploratória dos dados esta disponivel no [Google Colab](https://github.com/GabrielTrentino/WebScraping/blob/master/01-BooksToScrape/Books_To_Scrape.ipynb) e, em seguida, foram geradas as informações necessárias para as possíveis tomadas de decisão que a empresa busque utilizar. Tais como:

* Livros com estoques abaixo de 5 exemplares;
* Livros com estoques abaixos de 5 exemplares mas com boas notas (4 e 5 estrelas);
* Livros com estoques acima de 10 exemplares e com boas notas (4 e 5 estrelas);

## COMO RODAR NA SUA MÁQUINA:

1. Baixe o arquivo [`BooksToScrape.rar`](https://github.com/GabrielTrentino/WebScraping/blob/master/01-BooksToScrape/BooksToScrape.rar) e descompacte;
2. Em seguida, abra o Pycharm e selecione o projeto;
3. Rode o `main.py`;
4. O `main.py` utilizará as funções do `book_spider.py` e fará o crawl dos 1000 livros existentes;
5. Finalizando, o script escreverá um arquivo `.csv`.

# **Dúvidas e Redes Sociais:**
O repositório aumentará o seu tamanho de acordo com as realizações dos cursos. E claro, aceito recomendações de cursos, livros ou vídeos! Qualquer duvida me chame no [LinkedIn](https://www.linkedin.com/in/gabriel-trentino-froes-415558144/).
