from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random
import time

service = Service(executable_path='driver/chromedriver.exe')
driver = webdriver.Chrome(service=service)

hoteis = {'nomes':[], 'endereco_fisico':[], 'primeiro_dominio':[]}
url = "https://www.riograndedosulhotels.net/search/?sort=Rating&order=DESC&part=1&Stars%5B%5D=0&Name="
driver.get(url)
html = driver.page_source

try:
    nomes_dos_hoteis = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hotel__link')))
    for nome_do_hotel in nomes_dos_hoteis:
        hoteis['nomes'].append(nome_do_hotel.text)

    elementos_p = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//p[@class='address']")))

    for elemento_p in elementos_p:
        endereco = elemento_p.text.replace(elemento_p.find_element(By.XPATH, "./i").text, "").strip()
        hoteis['endereco_fisico'].append(endereco.replace(' (Para o mapa)', ''))
except:
    print('Erro na extração dos nomes e endereço no site hoteleiro.')

pesquisar = [nome + ' ' + endereco for nome, endereco in zip(hoteis['nomes'], hoteis['endereco_fisico'])]
for termo_de_pesquisa in pesquisar:
    termo_de_pesquisa = termo_de_pesquisa.replace(" ", "+")
    url_do_google = f"https://www.google.com/search?q={termo_de_pesquisa}"
    driver.get(url_do_google)

    try:
        elemento_a = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@jsname="UWckNb"]')))
        link_do_elemento_a = elemento_a.get_attribute('href')
        hoteis['primeiro_dominio'].append(link_do_elemento_a)
    except:
        print('Erro na extração do endereço digital dos sites.')

driver.quit()

nome_arquivo_csv = 'saida.csv'
with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(hoteis.keys())
    escritor_csv.writerows(zip(*hoteis.values()))

print(f'O arquivo CSV "{nome_arquivo_csv}" foi criado com sucesso.')