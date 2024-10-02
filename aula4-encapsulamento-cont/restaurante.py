# restaurante.py
class Restaurante:
    def __init__(self,pedido= 0):
        self.__pedido = pedido
        
    def novoPedido(self):
            self.__pedido += 1
    def cancelarPedido(self):
        if self.__pedido >= 1:
            self.__pedido = self.__pedido - 1
        else:
            print("Não há nenhum pedido")
            
        
    def exibirPedidos(self):
       print(f"O numero de pedidos: {self.__pedido}")