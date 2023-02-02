from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

# def grafico(request):
#     valores = {}
#     aux = 0
#     for i in range(27):
#         for mes in range(12):
#             df = pd.read_csv(f'C:/Users/marco/Downloads/EstadosFinal/estado{i+1}/hipertensao_diabetes/mes'+str(mes+1)+'.csv', encoding="mbcs")
#             df2 = df.max()
#             df3 = df2.max()
#             dff = df3[-2::]
#             valores[aux] = dff
#             aux = aux+1
#     pacote = {"chave": valores}
#     return render(request, 'grafico.html',pacote)

def grafico(request):
    pacote = {}
    vetor = []
    a = 0
    for i in range(27):
        for mes in range(12):
            df = pd.read_csv(f'C:/Users/marco/Documents/GitHub/susana-bot/teste/EstadosFinal/estado{i+1}/hipertensao_diabetes/mes'+str(mes+1)+'.csv', encoding="mbcs") 
            df2 = df.max()
            df3 = df2.max()
            dff = df3[-2::]
            vetor.append (dff)
            a  += 1
    pacote = {"chave": vetor}
    #print(pacote)
    print(len(vetor))
    return render(request, 'grafico.html', pacote)