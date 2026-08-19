import threading
class Conta:
    def __init__(self):
        self.saldo_central = 0
        self.lock = threading.Lock()
        
    def somarCaixa(self, valor):
        with self.lock: #exclusao mutua 
            for i in range(1000):
                self.saldo_central += valor

if __name__ == "__main__":
    conta = Conta()

    caixa01 = threading.Thread(target=conta.somarCaixa,args=(10,))
    caixa02 = threading.Thread(target=conta.somarCaixa,args=(10,))
    caixa03 = threading.Thread(target=conta.somarCaixa,args=(10,))
    caixa04 = threading.Thread(target=conta.somarCaixa,args=(10,))
    caixa05 = threading.Thread(target=conta.somarCaixa,args=(10,))
 
    caixa01.start()
    caixa05.start()
    caixa04.start()
    caixa03.start()
    caixa02.start()
    
    caixa01.join()
    caixa02.join()
    caixa03.join()
    caixa04.join()
    caixa05.join()

    print(conta.saldo_central)