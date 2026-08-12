import threading
import time

def minha_tarefa(param):
    t = threading.current_thread()
    for i in range(0, 10):
        print(f"Thread {t.name} | ID interno: {threading.get_ident()} | Param: {param}")
        time.sleep(1)

t1 = threading.Thread(target=minha_tarefa, args=("A",), name="Tarefa-1")
t2 = threading.Thread(target=minha_tarefa, args=("B",), name="Tarefa-2")

t1.start()
t2.start()