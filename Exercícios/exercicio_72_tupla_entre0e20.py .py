# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Exemplo:
# Digite um número: 9
# Nove
# Digite um número: 3
# Três

from colorama import Fore, Style, init
init(autoreset=True)

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f'{Fore.CYAN}Você digitou o número: {tupla[numero]}.')
        break
    else:
        print(f"{Fore.RED}Número inválido. Digite um número entre 0 e 20.{Style.RESET_ALL}")
        print(f'{Fore.BLUE}Tente novamente.{Style.RESET_ALL}')
        print()
