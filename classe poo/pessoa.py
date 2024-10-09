class Pessoa:
    #Atributos - características da classe
    nome = "Fulano" 
    idade = 25 
    altura = 1.60
    
    #Métodos comportamentos da classe
    def falar(self,texto):# self é um parametro obrigatótio do python que informa que o método pertence a própria classe foi criada.
        print(f"Tenho algo para te falar: {texto}")

#Criando objetos 
Pessoa1 = Pessoa()# Dessa forma estamos criando um objeto do tipo pessoa

print(Pessoa1.nome, Pessoa1.idade)
Pessoa1.falar("Bom dia, hoje é segunda-feira")