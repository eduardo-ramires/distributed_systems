import threading
import time

lista_numeros = []
lista_nomes = []

def tarefa_numeros(param):
    t = threading.current_thread()
    print(f"Thread {t.name} | Lendo arquivo {param}...")
    with open(param, "r", encoding="utf-8") as f:
        global lista_numeros
        lista_numeros = [int(linha.strip()) for linha in f]
    time.sleep(1)
    print(f"Thread {t.name} | Exibindo lista de números: {lista_numeros}")

def tarefa_nomes(param):
    t = threading.current_thread()
    print(f"Thread {t.name} | Lendo arquivo {param}...")
    with open(param, "r", encoding="utf-8") as f:
        global lista_nomes
        lista_nomes = [linha.strip() for linha in f]
    time.sleep(1)
    print(f"Thread {t.name} | Exibindo lista de nomes: {lista_nomes}")

t1 = threading.Thread(target=tarefa_numeros, args=("numeros.txt",), name="Tarefa-Numeros")
t2 = threading.Thread(target=tarefa_nomes, args=("nomes.txt",), name="Tarefa-Nomes")

t1.start()
t2.start()

t1.join()
t2.join()