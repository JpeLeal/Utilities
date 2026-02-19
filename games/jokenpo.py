import time
import random

# primeira tentativa de criar um código decente sozinho
# tentativa de fazer um mini bot que dê opção de jogos como jogo da velha ou jokenpô

#primeiro definir qual a opção
jogo = 3
jogo1 = "Jokenpô"
jogo2 = "Forca"

#Inicializando o jogo.
print("Inicializando o jogo...")
time.sleep(1)

jogador = input("Olá, que bom tê-lo aqui. Qual seu nome?  -> ").strip()

while jogo == 3:
    opcoes_jogo = [1, 2, 3]
    jogo = input(f"Olá! {jogador}! O que vamos jogar hoje? temos duas opções: 1.Jokenpô.  2.Forca.  3.Voltar ao início.  ->")
    jogo = int(jogo)
    if jogo not in opcoes_jogo:
        print("Selecione uma opção válida!")
        jogo = 3
        continue
    elif jogo == 1:
        print(f"Vamos jogar {jogo1}!")
    elif jogo == 2:
        print(f"Vamos jogar {jogo2}!")


#inicio do jogo jokenpô


while jogo == 1:
    print(f"Vamos começar! Se prepare!")
    jogada = input(
        "Selecione sua jogada: "
        "Pedra | "
        "Papel |  "
        "Tesoura |  -> "
        ).strip().lower()
    if jogada not in ["pedra", "papel", "tesoura"]:
        print("Selecione uma opção válida!")
        continue
    
        
    time.sleep(1)
    print("Jo...")
    time.sleep(1)
    print("Ken...")
    time.sleep(1)
    print("Pô!")
    time.sleep(2)
    
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
    jogo = input("Vamos jogar novamente? 1.Jogar jokenpô novamente.|  3. para voltar ao início.")
    jogo = int(jogo)
    if jogo not in opcoes_retorno:
        print("Selecione uma opção válida!")

    




    
    


