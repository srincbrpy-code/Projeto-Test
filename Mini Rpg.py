import random
import time



print("Bem-vindo ao novo campo de batalha!")
time.sleep(2)
jogador = input("Digite seu nome de jogador: ")
print(f"\nBem-vindo, |{jogador}|")
time.sleep(2)

class Monstro:
    def __init__(self, nome, vida, ataque, defesa, nivel):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel

    def subir_nivel(self):
        self.nivel += 1
        self.vida += self.vida / 4
        self.ataque += self.ataque / 4
        self.defesa += self.defesa / 4
        self.mana += self.mana / 4
        print(f"{self.nome} subiu para o nível {self.nivel}!")
    
    def atributos_M(self):
        print(f"Nome: {self.nome}\nVida: {self.vida}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\nNível: {self.nivel}")



class Personagem:
    def __init__(self, nome, classe, vida, ataque, defesa, mana, magia, nivel, experiencia):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.mana = mana
        self.magia = magia
        self.nivel = nivel
        self.experiencia = experiencia

    def subir_nivel(self):
        self.nivel += 1
        self.vida += self.vida / 4
        self.ataque += self.ataque / 4
        self.defesa += self.defesa / 4
        self.mana += self.mana / 4
        self.magia += self.magia / 4
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def atributos(self):
        print(f"Nome: {self.nome}\nClasse: {self.classe}\nVida: {self.vida}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\nMana: {self.mana}\nMagia: {self.magia}\n \nNível: {self.nivel}\nExperiência: {self.experiencia}")
    

class Guerreiro(Personagem):
    def __init__(self):
        super().__init__(self.nome, classe="Guerreiro", vida=15, ataque=7, defesa=5, mana=10, magia=0, nivel=1, experiencia=0)

class Mago(Personagem):
    def __init__(self):
        super().__init__(self.nome, classe="Mago", vida=10, ataque=2, defesa=2, mana=60, magia=7, nivel=1, experiencia=0)

arma = ""

classe_escolhida = input("Digite o número da classe desejada: \n1 - Guerreiro\n2 - Mago\n [Digite aqui]: ")
if classe_escolhida == "1":
    jogador = Guerreiro
    class Atributo_Fisico(Personagem):
            def __init__(self):
                while True:
                    tipo_arma = input("Escolha uma arma para seu ataque especial:\n1 - Espada Longa\n2 - Sabre")
                    if tipo_arma == "1":
                        print(f"{self.nome} é um guerreiro com Espada Longa!")
                        arma = "Espada Longa"
                        break
                    elif tipo_arma == "2":
                        print(f"{self.nome} é um guerreiro com Sabre!\n Bonus: Chance de esquiva aumentada!")
                        tipo_arma = "Sabre"
                        break
                    else:
                        print("Arma inválida! Tente novamente.")
elif classe_escolhida == "2":
    jogador = Mago
    class Atributo_elemental(Personagem):
        def __init__(self):
            while True:
                elemento = input("Escolha um elemento para seu ataque especial:\n1 - Fogo\n2 - Água\n3 - Terra\n4 - Ar\n [Digite aqui]: ")
                if elemento == "1":
                    print(f"{self} é um mago de Fogo! Você recebeu um bonus de magia!")
                    self.magia += 2
                elif elemento == "2":
                        print(f"{self} é um mago de Água! Você recebeu um bonus de vida!")
                        self.vida += 2
                elif elemento == "3":
                        print(f"{self} é um mago de Terra! Você recebeu um bonus de defesa!")
                        self.defesa += 2
                elif elemento == "4":
                        print(f"{self} é um mago de Ar! Você recebeu um bonus de mana!")
                        self.mana += 2
                else:
                        print("Elemento inválido! Tente novamente.")

goblin = Monstro(nome="Goblin", vida=7, ataque=4, defesa=3, nivel=1)
esqueleto_escudeiro = Monstro(nome="Esqueleto", vida=5, ataque=6, defesa=4, nivel=1)

monstros = [goblin, esqueleto_escudeiro]

taxa_mana_recuperacao = 5

def main():
    time.sleep(2)
    monstro1 = random.choice([goblin, esqueleto_escudeiro])
    apM2 = random.randint(1,2)
    if apM2< 2:
        monstro2 = random.choice([goblin, esqueleto_escudeiro])
        print(f'Um {monstro2.nome} apareceu!')
    while True:
        time.sleep(2)
        print(f'Oponentes: {monstro1.atributos_M()}\n{monstro2.atributos_M()}\nJogador>{jogador.atributos()}')
        acao = input("Você deseja (a) atacar, (e) ver atributos ou (s) fugir? ").lower()
        if acao == 'a':

            if jogador.classe == "Mago" and jogador.mana >= 10:
                    if jogador.mana < 60:
                        jogador.mana += taxa_mana_recuperacao
                    if jogador.mana > 60:
                        jogador.mana = 60
                    dano_magico = jogador.magia + random.randint(-3,3)
                    dano_magico_monstro1 = dano_magico - monstro1.defesa
                    dano_magico_monstro2 = dano_magico - monstro2.defesa
                    if dano_magico_monstro1 < 0:
                        monstro1.vida -= 0
                    if dano_magico_monstro2 < 0:
                        monstro2.vida -= 0
                    else:
                        monstro1.vida -= dano_magico_monstro1
                        monstro2.vida -= dano_magico_monstro2
                    jogador.mana -= 10
                    ataque_grupo = monstro1.ataque + monstro2.ataque - jogador.defesa * len(monstros)
                    jogador.vida -= ataque_grupo
                    print(f'Você causou {dano_magico} de dano mágico ao {monstro1.nome} e ao {monstro2.nome}!')
            elif jogador.classe == "Mago" and jogador.mana < 10:
                print("Mana insuficiente para ataque mágico! Realizando ataque físico.")
                monstro1.vida -= jogador.ataque + random.randint(-3,3) - (monstro1.defesa)
                monstro2.vida -= jogador.ataque + random.randint(-3,3) - (monstro2.defesa)
                print(f'Você causou {jogador.ataque} de dano ao {monstro1.nome} e ao {monstro2.nome}!')
            elif jogador.classe == "Guerreiro":
                if tipo_arma == "Guerreiro":
                    dano_fisico = jogador.ataque + random.randint(-3,3)
                
                else:
                    dano_fisico -= monstro1.defesa
                if dano_fisico < 0:
                    monstro1.vida -= 0
                    monstro2.vida -= 0
                else:
                    monstro1.vida -= dano_fisico
                monstro2.vida -= dano_fisico
            print(f'Você causou {dano_fisico} de dano ao {monstro1.nome} e ao {monstro2.nome}!')

        elif acao == 'e':
            print(f'{jogador.atributos()}')
        elif acao == 's':
            print("FRACO! Volte aqui! Não seja um covarde!")
            break
        else:
            print("Ação inválida! Tente novamente.")



if __name__ == "__main__":
    main()