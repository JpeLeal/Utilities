import time
import os


def cls(): #função para limpar a tela, funciona tanto para windows quanto para linux
    os.system('cls' if os.name == 'nt' else 'clear')

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
print(forca_desenho[0])
time.sleep(3)
cls()

print(forca_desenho[1])
time.sleep(1.5)
cls()