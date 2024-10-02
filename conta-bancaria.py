class Conta: 
    #metódo construtor
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #criando os demais métodos
    def detalhes(self):
        print(f"Olá {self.titular} seu saldo atual é {self.saldo}")