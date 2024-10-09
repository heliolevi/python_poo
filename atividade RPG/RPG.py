class Personagem:
    def __init__(self,nome,vida = 5):
        self._nome = nome 
        self._vida = vida
    def atacar(self):
        print("O personagem está atacando")
    
    
class Jogador(Personagem):
    def __init__(self,nome,vida,raca,):
        super().__init__(nome,vida)
        self._raca = raca
        self._iventario = []
        
    def usarHabilidade(self,poder):
        print(f"O jogador {self._nome} usou a skill {poder}")
    def exibirPerso(self):
        print(f" Nome : {self._nome}\n Raça: {self._raca}")
    
    def coletarItem(self,item):
        self._iventario.append(item)
        print(f"o item {item} foi coletado(a).\n Inventario: \n{self._iventario} ")
    
class Monstro(Personagem):
    def __init__(self,nome,vida,tipo,forca = 20):
        super().__init__(nome,vida) #super:é pra pegar atributo da classe mãe
        self._tipo = tipo
        self._forca = forca
    print("Um monstro foi invocado")
    def exibirInfo(self):
        print(f" O monstro {self._nome} apareceu!\n Atributos:\n tipo: {self._tipo} \n vida: {self._vida} \n força:{self._forca}")
 
    def invocarAliado(self, nomeAliado,tipoAliado):
        print(f"Monstros aliados invocados. Derrote-os!!! \n Monstros Invocados: \n nome : {nomeAliado}\n tipo: {tipoAliado} \n vida: {self._vida} \n força:{self._forca}")
    
    def Defender(self):
        self._vida = self._vida - 1
        print(f"O monstro se defendeu!!. \n vida: {self._vida}")
