class Pessoa:
    #Atributos o método construtor 
    def __init__(self, nome, hobby, endereco):
        #Estamos criando atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parãmetros que srão usados como atributos
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco
    #Criando os métodos normais 
    def  exibirDados(self):
        print(f"Olá {self.nome} seu hobby é {self.hobby} e seu endereço é {self.endereco}")

#Criando os objetos 
pessoa1 = Pessoa("Geraldo","Corredor","Rua 10 Cohab")
pessoa1.exibirDados()

pessoa2 = Pessoa("Karla", "Artes Marciais", "Av")