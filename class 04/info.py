from concurrent.futures import ThreadPoolExecutor
import threading
import time 

num_filiais = 18
tamanho_lista = 10

# Listas globais para armazenar os resultados por filial e status
resultados_0 = [0] * num_filiais
resultados_1 = [0] * num_filiais
resultados_2 = [0] * num_filiais
resultados_3 = [0] * num_filiais

lock = threading.Lock()

def processar_filial(indice, num_itens):
    try:
        with open("erro.log", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        contagem_0 = 0
        contagem_1 = 0
        contagem_2 = 0
        contagem_3 = 0

        for linha in linhas:
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(",")
            if len(partes) < 4:
                continue

            status = partes[2]

            if status == "0":
                contagem_0 += 1
            elif status == "1":
                contagem_1 += 1
            elif status == "2":
                contagem_2 += 1
            elif status == "3":
                contagem_3 += 1
        with lock:
            resultados_0[indice] = contagem_0
            resultados_1[indice] = contagem_1
            resultados_2[indice] = contagem_2
            resultados_3[indice] = contagem_3

    except FileNotFoundError:
        print(f"[Erro] O arquivo 'erro.log' não foi encontrado para a filial {indice + 1}.")


def somar_total():
    print("\n" + "=" * 40)
    print(f"Resultados de Status 0 por filial: {resultados_0}")
    print(f"Resultados de Status 2 por filial: {resultados_2}")
    print(f"Total geral de ocorrências (Status 0): {sum(resultados_0)}")
    print("=" * 40)


if __name__ == "__main__":
    # Marca o tempo de início antes de disparar as threads
    tempo_inicio = time.perf_counter()

    # Executando o processamento em paralelo para cada filial
    with ThreadPoolExecutor(max_workers=num_filiais) as pool:
        for i in range(num_filiais):
            pool.submit(processar_filial, i, tamanho_lista)

    # Executando a thread de totalização após todas as filiais terminarem
    t_total = threading.Thread(target=somar_total)
    t_total.start()
    t_total.join()

    # Marca o tempo de término após todas as operações finalizarem
    tempo_fim = time.perf_counter()
    tempo_total = tempo_fim - tempo_inicio

    print(f"Tempo total de execução: {tempo_total:.4f} segundos")