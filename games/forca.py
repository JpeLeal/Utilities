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
            "6. Aleatório (Palavra e dificuldade aleatórios)\n " \
            "7. Retornar ao menu principal -> ")
        cls()
        if categoria_escolhida not in ["1", "2", "3", "4", "5", "6", "7"]: #escolhendo categoria para depois ser comparada no index
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
                start_game = True # variável que vai definir se o jogo vai começar ou não
                chances = 0 #definindo o número de chances do jogador

        elif categoria_escolhida == 7: #definindo retorno ao menu principal
            star_game = False
            opcao = 3
            return opcao
        else:
            categoria_escolhida = categoria[int(categoria_escolhida) -1] #ajustando para a indexação do python.
            linha = random.choice( list(csv.reader(open(f"games/palavras/{categoria_escolhida}.csv")))) #escolhe uma linha aleatória dentro do csv da categoria escolhida
            palavra = linha[0] #retorna a palavra
            dificuldade = linha[1] #retorna a dificuldade
            start_game = True # variável que vai definir se o jogo vai começar ou não
            chances = 0 #definindo o número de chances do jogador

        while start_game: #ínicio do jogo de fato

            if dificuldade == "facil": # Mensagens do header de acordo com a dificuldade
                mensagem_dificuldade = "Vai ser moleza!"
            elif dificuldade == "media":
                mensagem_dificuldade = "Boa Sorte!"
            elif dificuldade == "dificil":
                mensagem_dificuldade = "Vamos ver como vai ser sair!"
            
            topo = f"Seu desafio tem a dificuldade {dificuldade}! {mensagem_dificuldade}" #definição do header        
            cls()

            forca_desenho = ["""
+----+
|
|
|
|
=============
            """,
            """
+----+
|    O
|
|
|
=============
            """, """
+----+
|    O
|   /
|
|
=============
            """, """
+----+
|    O
|   /|
|
|
=============
            """,
            """
+----+
|    O
|   /|\  
|
|
=============
            """,
            """
+----+
|    O
|   /|\  
|   / 
|
=============
            """,
            """
+----+
|    O
|   /|\  
|   / \  
|
=============
            """]

            cls()
            print(topo) #header que vai ficar sempre mostrando o nível da palavra        
            print(forca_desenho[chances]) #desenho da forca             
            alfabeto = "abcdefghijklmnopqrstuvwxyz" #letras aceitas
            letras_ocultas = ["_"] * len(palavra)
            print(f"Dica: {categoria_escolhida}")
            print(palavra)
            print(" ".join(letras_ocultas))
            print()
            tentativa = input(f"Digite uma letra: -> ")
            if len(tentativa) != 1 or tentativa not in alfabeto: #caso a entrada não seja uma unica letra, vai retornar sem perder vida
                print("Digite apenas uma letra, sem acentos! ")
                time.sleep(2)
                continue
            elif tentativa not in palavra: #caso seja apenas uma letra mas não exista na palavra, perde uma vida
                print("Não temos essa letra nesta palavra!")
                time.sleep(2)
                chances += 1
                if chances == 5: #Aviso da ultima chance
                    print("Essa é a última chance em!")
                    time.sleep(2)
                    continue
                elif chances == 6: #condição de derrota
                    print(f"Você perdeu! a palavra era: {palavra}")
                    time.sleep(2)
                    cls()
                continue

            elif tentativa in palavra: #condição de acerto
                print("Bom palpite, essa letra existe!")
                time.sleep(2)
                continue

            
            cls()
            break

