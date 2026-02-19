import time
import random
from menu import menu
from jokenpo import jokenpo

jogos_disponiveis = [ "Jokenpô", "Forca" ]
# primeira tentativa de criar um código decente sozinho
# tentativa de fazer um mini bot que dê opção de jogos como Forca ou Jokenpô
while True:
    opcao = menu()
    time.sleep(1)
    if opcao == 1:
        print(f"Vamos jogar {jogos_disponiveis[0]}!")
        jokenpo()
    elif opcao == 2:
        print("Em breve teremos o jogo da Forca! Fique ligado!")
        time.sleep(2)
    elif opcao == 3:
        print("Voltando ao início...")
        time.sleep(1)
    elif opcao == 4:
        print("Saindo do jogo...")
        time.sleep(1)
        break






    
    


