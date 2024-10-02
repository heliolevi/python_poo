from contabancaria import Conta

minhaConta = Conta(123,"Ermenegildo Sousa",1000,)
minhaConta.detalhes() 

minhaConta.saldo = 20000
minhaConta.detalhes()

print(f"O limite atual é {minhaConta.getLimite()}")
minhaConta.setLimite(259)
print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(100)
minhaConta.detalhes()
minhaConta.saca(500)
minhaConta.detalhes()
