import threading
import random

# Gera 10.000 números inteiros aleatórios
numeros = [random.randint(1, 100) for _ in range(10000)]

resultados = [0, 0, 0, 0]

# calcula e guarda o resultado 
def somar_parte(sublista, indice):
    resultados[indice] = sum(sublista)

# Divide a lista em 4 partes
tamanho = len(numeros) // 4
partes = [numeros[i * tamanho:(i + 1) * tamanho] for i in range(4)]

t1 = threading.Thread(target=somar_parte, args=(partes[0], 0))
t2 = threading.Thread(target=somar_parte, args=(partes[1], 1))
t3 = threading.Thread(target=somar_parte, args=(partes[2], 2))
t4 = threading.Thread(target=somar_parte, args=(partes[3], 3))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

#soma total
soma_total = sum(resultados)
print("Soma total:", soma_total)