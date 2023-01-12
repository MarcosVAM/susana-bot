from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
import pandas as pd
#importando o selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import codecs
import os

# parte do código do gráfico 
def grafico(request):
    valores = {}
    for i in range(12):
        df = pd.read_csv(f'mes{i+1}.csv', encoding="mbcs")
        df2 = df.max()
        df3 = df2.max()
        dff = df3[-2::]
        valores[i] = dff
    pacote = {"chave": valores}
    return render(request, 'grafico.html', pacote)

# a partir daqui já é a função de baixar as tabelas do bot

def seleciona(request):
    return render(request, "selecionar.html")

#selecionando o conteudo das tabelas
def selecionador(id, index, deselect, driver):

    select_element = driver.find_element(By.ID,id)
    select_object = Select(select_element)
    select_object.select_by_index(index)
    #caso o select seja multiple colocar true
    if deselect:
        select_object.deselect_by_index(0)


#selecionar tabelade acordo com o index(so precisa mudar os numeros para mudar o conteudo baixado)


#clicar no botao


def clicker_by_name(nome, driver):
    print(driver)    
    botao = driver.find_element("name", nome)
    botao.click() 


def teste(request, v1, v2, v3, v4):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/nruf.def")

    selecionador("L", v1, False, driver)
    selecionador("C", v2, False, driver)
    selecionador("I", v3, True, driver)
    selecionador("A", v4, True, driver)
    clicker_by_name("mostre", driver)
    time.sleep(5)
    #selecionar o primeiro botao( que no caso é o csv)

    csv = driver.find_element(By.CLASS_NAME, "botao_opcao")
    csv.click()

    caminho = "C://Users//marco//Downloads"
    lista_arquivos = os.listdir(caminho)



    lista_datas = []
    for arquivo in lista_arquivos:
        # descobrir a data desse arquivo
        if ".csv" in arquivo:
            data = os.path.getmtime(f"{caminho}/{arquivo}")
            lista_datas.append((data, arquivo))
        
        # data inicial = 01/01/2021
        # data1 = 02/01/2021 -> 10.000
        # data2 = 15/02/2021 -> 150.000
        
    lista_datas.sort(reverse=True)
    ultimo_arquivo = lista_datas[0]
    
    
    #o tamanho max de bits que o codigo vai ler
    blockSize = 1048576
    resposta = ""
    #laço que vai pegar o arquivo baixado lá da pasta downloads
    with codecs.open(f"C://Users//marco//Downloads//{ultimo_arquivo[1]}","r",encoding="mbcs") as sourceFile:
        #laço que vai transcrever o arquivo para outro arquivo na pasta kidnapper no formato de UTF - 8
        with codecs.open("teste.csv","w",encoding="UTF-8") as targetFile:
            while True:
                contents = sourceFile.read(blockSize)
                resposta = resposta + str(contents)
                if not contents:
                    break
                targetFile.write(contents)

    time.sleep(10)
    return HttpResponse(resposta)
    # return render(request, "Core/upload-file.html")








# Create your views here.
