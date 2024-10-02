class Carro:
    def __init__(self, marca, modelo, ano, preco_diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco_diaria = preco_diaria

    def exibirDetalhes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço Diária: R${self.preco_diaria:.2f}')

    def calcularPrecoAluguel(self, dias):
        return dias * self.preco_diaria



    