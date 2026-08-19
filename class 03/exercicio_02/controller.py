import threading
import model
import view

def executar():
    filial_1, filial_2, filial_3, filial_4 = model.gerar_dados()
    resultado = [0] * 4

    soma_filial_1 = threading.Thread(target=model.popular_lista, args=(filial_1, 0, resultado, view.exibir_soma))
    soma_filial_2 = threading.Thread(target=model.popular_lista, args=(filial_2, 1, resultado, view.exibir_soma))
    soma_filial_3 = threading.Thread(target=model.popular_lista, args=(filial_3, 2, resultado, view.exibir_soma))
    soma_filial_4 = threading.Thread(target=model.popular_lista, args=(filial_4, 3, resultado, view.exibir_soma))

    soma_filial_1.start()
    soma_filial_2.start()
    soma_filial_3.start()
    soma_filial_4.start()

    soma_filial_1.join()
    soma_filial_2.join()
    soma_filial_3.join()
    soma_filial_4.join()

    somar_total = threading.Thread(target=model.somar_total, args=(resultado, view.exibir_total))
    somar_total.start()
    somar_total.join()

if __name__ == "__main__":
    executar()