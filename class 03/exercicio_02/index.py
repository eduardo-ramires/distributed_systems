import random
import threading

def somar_total(resultados):
    total_geral = sum(resultados)
    print('Total:', total_geral )

def popular_lista(lista, indice, resultado):
    soma = 0;
    for i in range(10):
        soma = soma + lista[i]
    resultado[indice] = soma
                
    print('Soma:', soma )

if __name__ == "__main__":
    filial_1 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_2 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_3 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    filial_4 = [round(random.uniform(100, 5000), 2) for _ in range(10)]
    resultado = [0] * 4

    soma_filial_1 = threading.Thread(target=popular_lista,args=(filial_1, 0, resultado))
    soma_filial_2 = threading.Thread(target=popular_lista,args=(filial_2, 1, resultado))
    soma_filial_3 = threading.Thread(target=popular_lista,args=(filial_3, 2, resultado))
    soma_filial_4 = threading.Thread(target=popular_lista,args=(filial_4, 3, resultado))

    soma_filial_1.start()
    soma_filial_2.start()
    soma_filial_3.start()
    soma_filial_4.start()

    soma_filial_1.join()
    soma_filial_2.join()
    soma_filial_3.join()
    soma_filial_4.join()

    somar_total = threading.Thread(target=somar_total, args=(resultado,))
    somar_total.start()
    somar_total.join()