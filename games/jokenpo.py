import time
import random
import os

def cls(): #definindo a função de limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')

def jokenpo():
    print("Iniciando Jokenpô...")
    time.sleep(1.5)
    cls()
    opcao = 1
    while opcao == 1:
        print(f"Vamos começar! Se prepare!")
        jogada = input(
            "Selecione sua jogada:\n "
            "-Pedra\n "
            "-Papel\n "
            "-Tesoura\n-> "
            ).strip().lower()
        cls()
        if jogada not in ["pedra", "papel", "tesoura"]:
            print("Selecione uma opção válida! ")
            continue
        
        time.sleep(1)
        print("Jo...")
        time.sleep(1)
        print("Ken...")
        time.sleep(1)
        print("Pô!")
        time.sleep(1.5)
    
        #Opções de mensagens de retorno.
        mensagem_vitoria = [
            "Parabéns! Você venceu!",
            "Droga! Dessa vez você ganhou!",
            "Nossa, que sorte! Você ganhou!",
            "Dá próxima não será tão fácil! Você ganhou!"
        ]
        mensagem_derrota = [
            "Ah, que pena! Você perdeu!",
            "HA! você perdeu!",
            "Nossa, que azar! Você perdeu!",
            "Dá próxima vê se melhora! Você perdeu!"
        ]
        mensagem_empate = [
            "Empatou! Vamos jogar novamente!",
            "Hmmm, você me imitou! Empatamos, vamos de novo!",
            "Nossa, que coincidência! Empatamos!",
            "Dá próxima não será tão fácil! Empatamos!"
        ]

        opcoes = [ "Pedra", "Papel", "Tesoura" ]

        jogada_bot = random.choice(opcoes)
        print(jogada_bot)
        time.sleep(1)
        if jogada == "pedra" and jogada_bot == "Tesoura":
            print(random.choice(mensagem_vitoria))
        elif jogada == "papel" and jogada_bot == "Pedra":
            print(random.choice(mensagem_vitoria))
        elif jogada == "tesoura" and jogada_bot == "Papel":
            print(random.choice(mensagem_vitoria))
        elif jogada == "pedra" and jogada_bot == "Papel":
            print(random.choice(mensagem_derrota))
        elif jogada == "papel" and jogada_bot == "Tesoura":
            print(random.choice(mensagem_derrota))
        elif jogada == "tesoura" and jogada_bot == "Pedra":
            print(random.choice(mensagem_derrota))
        elif jogada == jogada_bot.lower():
            print(random.choice(mensagem_empate))
        time.sleep(2)

        opcoes_retorno = [1, 3]
        while True:
            opcao = input("Vamos jogar novamente? \n 1.Jogar jokenpô novamente.\n 3.Para voltar ao início.  ")
            opcao = int(opcao)
            if opcao not in opcoes_retorno:
                print("Selecione uma opção válida!")
                cls()
                continue
            break