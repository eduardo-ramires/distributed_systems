import random
import threading

def gerar_dados():
    filial_1 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_2 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_3 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_4 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    return filial_1, filial_2, filial_3, filial_4

def popular_lista(lista, indice, resultado, callback_exibir):
    soma = 0
    for i in range(10):
        soma = soma + lista[i]
    resultado[indice] = soma
    callback_exibir(soma)

def somar_total(resultados, callback_exibir):
    total_geral = sum(resultados)
    callback_exibir(total_geral)