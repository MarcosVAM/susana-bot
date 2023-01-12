from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
import pandas as pd


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