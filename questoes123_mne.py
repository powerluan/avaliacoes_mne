# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:58:15 2020

@author: Luan Moreira

MÉTODOS PARA CÁLCULO DE RAÍZ
"""

import math

# Intervalo para análise
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))

# Escolha do método de cálculo da raíz
metodo = int(input("Selecione 1 para Bisseção, 2 para Posição Falsa e 3 para Posição Fixa: "))

# Método da Bisseção
if metodo == 1:
    # Função estudada
    def f(x):
        return 108 + (221.1 * (1 - math.exp(-11.4 * x))) - 300
    
    # Teorema de Bolzano
    if (f(a) * f(b)) < 0:
        print("Há pelo menos uma raíz")
        erro = 10**-3 # De acordo com a precisão requerida
        xbarra = (a + b) / 2
        i = 0
        while (abs(f(xbarra)) > erro) or (abs(b - a) > erro):
            if (f(a) * f(xbarra)) < 0:
                b = xbarra
                xbarra = (a + b) / 2
            else:
                a = xbarra
                xbarra = (a + b) / 2
            i = i + 1
        print("A raíz da equação no intervalo definido é {:.8f} e obteve {:d} iterações".format(xbarra,i))
    else:
        print("Não há raíz")

# Método da Posição Falsa
if metodo == 2:
    # Função estudada
    def f(x):
        return 108 + 221.1 * (1 - math.exp(-11.4 * x)) - 300
    
    # Teorema de Bolzano
    if (f(a) * f(b)) < 0:
        print("Há pelo menos uma raíz")
        erro = 10**-3 # De acordo com a precisão requerida
        xbarra = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        i = 0
        while (((f(a) * f(a+erro)) < 0) and ((f(b) * f(b+erro)) < 0)) or (abs(f(xbarra)) > erro):
            if (f(a) * f(xbarra)) < 0:
                b = xbarra
                xbarra = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
            else:
                a = xbarra
                xbarra = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
            i = i + 1
            
        print("A raíz da equação no intervalo definido é {:.8f} e obteve {:d} iterações".format(xbarra,i))
    else:
        print("Não há raíz")

# Método da Ponto Fixo
if metodo == 3:
    # Função estudada
    def f(x):
        return 108 + 221.1 * (1 - math.exp(-11.4 * x)) - 300
    
    def fder(x):
        return 2520.54 * math.exp(-11.4 * x)
    
    def q(x):
        return x - (f(x) / fder(x))
    
    erro = 10**-3 # De acordo com a precisão requerida
    i = 0
    while ((f(a) * f(a+erro)) > 0) or (abs(f(a)) > erro):
        a = q(a)
        i = i + 1
    
    print("A raíz da equação no intervalo definido é {:.8f} e obteve {:d} iterações".format(xbarra,i))
