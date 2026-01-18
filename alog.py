import random
import time

goblin = "Goblin"
print("Bem-vindo ao novo campo de batalha!")
time.sleep(2)
jogador = input("Digite seu nome de jogador: ")
print(f"\nBem-vindo, |{jogador}|")
time.sleep(2)
print(f'Pronto para a batalha contra um {goblin}?')
def main():
    vida_goblin = random.randint(20,27)
    vida_jogador = random.randint(20,27)
    while True:
            time.sleep(2)
            print(f'Vida do goblin> {vida_goblin}\n Sua vida> {vida_jogador}')
            acao = input("Você deseja (a) atacar ou (s) sair? ").lower()
            if acao == 'a':
                ataque_jogador = random.randint(1,6)

                ataque_goblin = random.randint(1,6)

                chance_de_espada = random.randint(1,4)

                dado_de_pontos = random.randint(1,20)
                
                if dado_de_pontos >= 11:
                    print('Ataque bem sucedido!')
                    time.sleep(2)
                    if chance_de_espada == 1:
                        ataque_jogador * 2
                        vida_goblin -= ataque_jogador * 2
                        print(f'Ataque crítico! Dano em dobro!\nO Goblin sofreu {ataque_jogador * 2} de dano!')
                    else:
                        vida_goblin -= ataque_jogador
                        print(f'Você causou {ataque_jogador} de dano ao Goblin!')
                elif dado_de_pontos < 11:
                    print('Ataque falhou!')
                    time.sleep(2)
                    vida_jogador -= ataque_goblin
                    print(f'O Goblin causou {ataque_goblin} de dano a você!')
            elif acao == 's':
                print("FRACO! Volte aqui! Não seja um covarde!")
                break
            else:
                print("Ação inválida! Tente novamente.")

            if vida_goblin <= 0:
                print(f"\nParabéns, {jogador}! Você derrotou o Goblin!")
                break
            elif vida_jogador <= 0:
                print(f"\nQue pena, {jogador}. Você foi derrotado pelo Goblin!")
                break

if __name__ == "__main__":
    main()