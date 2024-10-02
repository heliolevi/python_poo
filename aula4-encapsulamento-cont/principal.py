from funcionario import Funcionario

funcionario1 = Funcionario("Gerente", 3000)
print("Seu cargo é: ,", funcionario1.getCargo())


funcionario1.cargo = "supervisor"
funcionario1.cargo = ("Engenheiro")
print("Seu cargo atual é",funcionario1.getCargo())

print("seu salário atual é", funcionario1.salario)

funcionario1.salario = 5500
print("seu salário atual é", funcionario1.salario)