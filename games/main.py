import time
import random
from menu import menu,cls
from jokenpo import jokenpo
from forca import forca


jogos_disponiveis = [ "Jokenpô", "Forca" ]
# primeira tentativa de criar um código decente sozinho
# tentativa de fazer um mini bot que dê opção de jogos como Forca ou Jokenpô
while True:
    opcao = menu()
    time.sleep(1)
    cls()
    if opcao == 1:
        print(f"Vamos jogar {jogos_disponiveis[0]}!")
        cls()
        jokenpo()
    elif opcao == 2:
        print(f"Vamos jogar {jogos_disponiveis[1]}!")
        cls()
        forca()
    elif opcao == 3:
        print("Voltando ao início...")
        time.sleep(1)
        cls()
    elif opcao == 4:
        print("Saindo do jogo...")
        time.sleep(1)
        cls()
        break






    
    


