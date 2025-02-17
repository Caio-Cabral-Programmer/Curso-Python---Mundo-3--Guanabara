# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e indique o menor e o maior número gerado.

from random import randint
from colorama import Fore, Style, init
init(autoreset=True)

# # Forma 1 - Usando lista temporária
# numeros = []
# for _ in range(5):
#     numeros.append(randint(1, 100))
# numeros_aleatorios = tuple(numeros)
#
# # Forma 2 - Usando concatenação correta de tuplas
# numeros_aleatorios = ()
# for _ in range(5):
#     numeros_aleatorios += (randint(1, 100),)  # Note a vírgula para criar tupla

# Forma 3 - Usando compreensão (mais pythônica)
numeros_aleatorios = tuple(randint(1, 100) for _ in range(5))

print(f'{Fore.CYAN}Lista de números aleatórios gerados:{Style.RESET_ALL} {numeros_aleatorios}')
print(f'{Fore.CYAN}Menor número gerado:{Style.RESET_ALL} {min(numeros_aleatorios)}')
print(f'{Fore.CYAN}Maior número gerado:{Style.RESET_ALL} {max(numeros_aleatorios)}')
