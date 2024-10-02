class Funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.__salario = salario

    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, novoCargo):
        self.__cargo = novoCargo

'''Iremos utilizar uma forma única do python
para acessar atributos privados'''
@property
def salario(self):
  return self.__salario

@salario.setter
def salario(self, valor):
    self.__salario = valor