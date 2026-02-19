import time
import random



print("Inicializando o jogo...")
time.sleep(1)
jogador = input("Olá, que bom tê-lo aqui.\nQual seu nome?\n-> ").strip()

def menu(): #Definindo a função menu para escolha do jogo
    while True:
        opcoes_jogo = [1, 2, 3, 4]
        opcao = input(f"Olá! {jogador}! O que vamos jogar hoje?\nTemos essas opções:\n 1.Jokenpô.\n 2.Forca.\n 3.Voltar ao início.\n 4.Sair do jogo.\n ->")
        opcao = int(opcao)
        if opcao not in opcoes_jogo:
            print("Selecione uma opção válida!")
            time.sleep(1)
            opcao = 0
        elif opcao == 1:
            return opcao
        elif opcao == 2:
            return opcao
        elif opcao == 3:
            return opcao
        elif opcao == 4:
            return opcao
        