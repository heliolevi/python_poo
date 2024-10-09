# Capacidade de assumir várias formas, e somente em métodos.
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome 
        self._preco
        
    def descrever(self):
        print(f"O produto {self._nome} custa R$ {self._preco}")

    def calcularDesconto(self):
        pass

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self._autor = autor

    def descrever(self):
        print(f"O livro {self._nome} foi escrito por {self._autor}")

    def calcularDesconto(self):
        desconto = self._preco * 0,1