import threading
import time
import os

class ListaCompartilhada:
    def __init__(self):
        self.numeros = []
        self.lock = threading.Lock()

    def adicionar_numeros(self, um_numero):
        with self.lock:
            self.numeros.append(um_numero)
            print(f"{threading.current_thread().name} adicionou: {um_numero}")

    def retornar_numeros(self):
        with self.lock:
            return list(self.numeros)

def processar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            if linha_limpa: 
                try:
                    numero = int(linha_limpa)
                    lista.adicionar_numeros(numero)
                    time.sleep(0.05)
                except ValueError:
                    print(f"Valor inválido ignorado no arquivo {nome_arquivo}: '{linha_limpa}'")

if __name__ == "__main__":
    lista_compartilhada = ListaCompartilhada()

    arquivo_1 = "numeros.txt"
    arquivo_2 = "numeros_02.txt"

    t1 = threading.Thread(target=processar_arquivo, args=(lista_compartilhada, arquivo_1), name="Thread1")
    t2 = threading.Thread(target=processar_arquivo, args=(lista_compartilhada, arquivo_2), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nLista final:", lista_compartilhada.retornar_numeros())