class Funcionarios: 

     def __init__(self, nome, cargo, salario):
        self.nome = nome 
        self.cargo = cargo
        self.salario = salario
        
    #Criando métodos 
     def exebirDados(self):
            print(f"Olá {self.nome} seu cargo é {self.cargo}, parabens voce ganha uma peixinxa de {self.salario}")

     def verificarSalario(self):
            if self.salario <= 2000:
                print("Direito a bônus")
            else:
                print("Sem direito a bônus")

