import threading
from model import ContaModel
from view import ContaView

class ContaController:
    def __init__(self):
        self.model = ContaModel()
        self.view = ContaView()

    def executar_operacoes(self):
        caixa01 = threading.Thread(target=self.model.somarCaixa, args=(10,))
        caixa02 = threading.Thread(target=self.model.somarCaixa, args=(10,))
        caixa03 = threading.Thread(target=self.model.somarCaixa, args=(10,))
        caixa04 = threading.Thread(target=self.model.somarCaixa, args=(10,))
        caixa05 = threading.Thread(target=self.model.somarCaixa, args=(10,))
     
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

        self.view.exibir_saldo(self.model.saldo_central)

if __name__ == "__main__":
    controller = ContaController()
    controller.executar_operacoes()