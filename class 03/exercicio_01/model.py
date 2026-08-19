import threading

class ContaModel:
    def __init__(self):
        self.saldo_central = 0
        self.lock = threading.Lock()
        
    def somarCaixa(self, valor):
        with self.lock: # exclusao mutua 
            for i in range(1000):
                self.saldo_central += valor