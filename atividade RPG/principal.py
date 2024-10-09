from RPG import Personagem,Jogador,Monstro

personagem = Personagem("ktaros")
jogador = Jogador("ktaros",5,"Guerreiro")
monstro = Monstro("Vorath, O Devastador",20,"Orc",20)
monstroAlidado = Monstro("Besta",20,"Lobo",20)


monstro.exibirInfo()  
jogador.usarHabilidade("BERSERKER!!!")
monstro.Defender()
monstro.Defender()
monstroAlidado.invocarAliado("Besta","Lobo")
jogador.coletarItem("espada longa")
jogador.coletarItem("Poção de cura")