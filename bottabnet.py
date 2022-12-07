#importando o selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#acessar o site pelo CHROME
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://datasus.saude.gov.br/acesso-a-informacao/hipertensao-e-diabetes-hiperdia/")


def estados(nome):
    botao =  driver.find_element("name", nome)
    botao.click()
    
#estados("radiobutton")

def campo(id, index):
    select_element = driver.find_element(By.ID,id)
    select_object = Select(select_element)
    select_object.select_by_index(index)

#selecionando o conteudo das tabelas
def selecionador(id, index, deselect):
    select_element = driver.find_element(By.ID,id)
    select_object = Select(select_element)
    select_object.select_by_index(index)
#caso o select seja multiple colocar true
    if deselect:
       select_object.deselect_by_index(0)

#clicar no botao
def clicker_by_name(nome):    
    botao =  driver.find_element("name", nome)
    botao = driver.find_element("name", nome)
    botao.click()

for i in range(27):
    estados("radiobutton")
    campo("mySelect", i+1)
    for col in range (3):
        for con in range (4):
            for mes in range (12):
                selecionador("L", 0, False)
                selecionador("C", (col+1), False)       
                if con == 0:   
                        selecionador("I", (con), False) 
                else:
                        selecionador("I", (con), True)
                if i == 0 or i == 3 or i == 16 or i == 19 or i == 21:
                    selecionador("A", (27+mes), True)
                elif i == 6:
                        selecionador("A", (7+mes), True)
                elif i == 22:
                    selecionador("A", (26+mes), True)
                else:
                    selecionador("A", (28+mes), True)

                time.sleep(1)   
                clicker_by_name("mostre")
                time.sleep(1)
                try:
                    driver.find_element(By.XPATH,"//tbody//tr//td[@class='botao_opcao']")
                except:
                    driver.refresh()
                    driver.find_element(By.XPATH,"//tbody//tr//td[@class='botao_opcao']").click()
                else:
                    driver.find_element(By.XPATH,"//tbody//tr//td[@class='botao_opcao']").click()
                time.sleep(4)
                caminho = "C://Users//marco//Downloads"
                lista_arquivos = os.listdir(caminho)
                lista_datas = []
                for arquivo in lista_arquivos:
                # descobrir a data desse arquivo
                    if ".csv" in arquivo:
                        data = os.path.getmtime(f"{caminho}/{arquivo}")
                        lista_datas.append((data, arquivo))
                        lista_datas.sort(reverse=True)
                        ultimo_arquivo = lista_datas[0]
                        
                        if col == 0 and con == 0:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/regiao_de_saude_hipertensao/{ultimo_arquivo[1]}')
                        if col == 0 and con == 1:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/regiao_de_saude_diabetes_tipo1/{ultimo_arquivo[1]}')
                        if col == 0 and con == 2:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/regiao_de_saude_diabetes_tipo2/{ultimo_arquivo[1]}')
                        if col == 0 and con == 3:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/regiao_de_saude_hipertensao_diabetes/{ultimo_arquivo[1]}')
                        if col == 1 and con == 0:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/macrorregiao_de_saude_hipertensao/{ultimo_arquivo[1]}')
                        if col == 1 and con == 1:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/macrorregiao_de_saude_diabetes_tipo1/{ultimo_arquivo[1]}')
                        if col == 1 and con == 2:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/macrorregiao_de_saude_diabetes_tipo2/{ultimo_arquivo[1]}')
                        if col == 1 and con == 3:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/macrorregiao_de_saude_hipertensao_diabetes/{ultimo_arquivo[1]}')
                        if col == 2 and con == 0:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/divisao_estadual_hipertensao/{ultimo_arquivo[1]}')
                        if col == 2 and con == 1:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/divisao_estadual_diabetes_tipo1/{ultimo_arquivo[1]}')
                        if col == 2 and con == 2:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/divisao_estadual_diabetes_tipo2/{ultimo_arquivo[1]}')
                        if col == 2 and con == 3:
                            os.replace(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/Estados/estado{i+1}/divisao_estadual_hipertensao_diabetes/{ultimo_arquivo[1]}')
                        break
                time.sleep(4)
                driver.back()
                driver.refresh()
                 
    driver.get("https://datasus.saude.gov.br/acesso-a-informacao/hipertensao-e-diabetes-hiperdia/")
        

