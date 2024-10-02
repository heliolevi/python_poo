class Conta:
    #Método Construtor
    def __init__(self,numero,titular,saldo,limite = 200):#estamos passando um valor padrão para o limite, tornando opicional, dessa forma o objeto ao ser criado pode ter o limite informado ou não.
        #Quando colocamos 2 underline antes do nome do atributo, indicamos que esse atributo está com a visibilidade "privado",o contrário significa que está "público".
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    #Criando os demais métodos
    def detalhes(self):
            print(f"olá {self.__titular} seu saldo atual é {self.__saldo}") 
            
    def  getLimite(self):
        return self.__limite
    #Método que irá alterar o valor do limite
    def setLimite(self,valor):
        if valor < 0:
            print("informe um valor positivo para o limite")
        else:
            self.__limite = valor
        
    #Criando método para depositar valor
    def depositar(self,valor):
        if valor< 0:
            print("Informe um valor maior que zero")
        else:
            self.__saldo = self.__saldo + valor
     #Criar método para sacar valor
    def saca(self,valor):
        if self.__saldo <= 0 or valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo = self.__saldo - valor