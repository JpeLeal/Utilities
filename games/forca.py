import random
import csv
import time
import os

categoria = ["cor", "esporte", "frutas", "objeto", "paises"] #categorias disponíveis 

def cls(): #função para limpar a tela, funciona tanto para windows quanto para linux
    os.system('cls' if os.name == 'nt' else 'clear')

#definindo a função do jogo, o jogador primeiro escolhe a categoria e depois o jogo escolhe a palavra randomicamente e inicia o jogo mostrando a dificuldade da palavra.
def forca():
    print ("Iniciando a Forca...")
    time.sleep(1.5)
    cls()
    opcao = 2
    while opcao == 2:
        print(f"Vamos começar selecionando a categoria!")
        categoria_escolhida = input(
            "Selecione a categoria:\n "
            "1. Cor\n "
            "2. Esporte\n "
            "3. Frutas\n "
            "4. Objeto\n "
            "5. Paises\n "
            "6. Aleatório (Palavra e dificuldade aleatórios)-> ")
        cls()
        if categoria_escolhida not in ["1", "2", "3", "4", "5", "6"]: #escolhendo categoria para depois ser comparada no index
            print("Selecione uma opção válida! ")
            cls()
            continue
        categoria_escolhida = int(categoria_escolhida) # transformando a string em int
        if categoria_escolhida == 6: #Caso escolha jogo aleatório, a categoria e a palavra serão aleatórias, iniciando o jogo diretamente.
            jogo_aleatorio = True 
            while jogo_aleatorio:
                categoria_escolhida = (random.randint(1,5) - 1) #escolhe randomicamente e ja ajusta para a indexação 
                categoria_escolhida = categoria[categoria_escolhida] #redefinindo variável para a string da categoria escolhida
                linha = random.choice( list(csv.reader(open(f"games/palavras/{categoria_escolhida}.csv")))) #escolhe uma linha aleatória dentro do csv
                palavra = linha[0] #retorna a palavra
                dificuldade = linha[1] #retorna a dificuldade
                jogo_aleatorio = False
        else:
            categoria_escolhida = categoria[int(categoria_escolhida) -1] #ajustando para a indexação do python.
            linha = random.choice( list(csv.reader(open(f"games/palavras/{categoria_escolhida}.csv")))) #escolhe uma linha aleatória dentro do csv da categoria escolhida
            palavra = linha[0] #retorna a palavra
            dificuldade = linha[1] #retorna a dificuldade
        
        if dificuldade == "facil":
            mensagem_dificuldade = "Vai ser moleza!"
        elif dificuldade == "media":
            mensagem_dificuldade = "Boa Sorte!"
        elif dificuldade == "dificil":
            mensagem_dificuldade = "Vamos ver como vai ser sair!"
        
        print(f"A palavra escolhida tem a dificuldade {dificuldade}! {mensagem_dificuldade}")
        time.sleep(2.5)
        cls()



