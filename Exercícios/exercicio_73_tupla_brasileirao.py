# Crie uma brasileirao preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
from colorama import Fore, Style, init
init(autoreset=True)

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Santos', 'Grêmio', 'Athletico-PR', 'Cruzeiro', 'Fluminense', 'Corinthians', 'Chapecoense', 'Cearál', 'Vasco da Gama', 'Atlético-GO', 'Bahia', 'Sport Recife')

print(30 * '=-=')
print(f'{Fore.CYAN}Lista de times do Campeonato Brasileiro de Futebol:{Style.RESET_ALL}{brasileirao}')
print(30 * '=-=')
print(f'{Fore.CYAN}Os 5 primeiros times são:{Style.RESET_ALL} {brasileirao[:5]}')
print(30 * '=-=')
print(f'{Fore.CYAN}Os últimos 4 colocados são:{Style.RESET_ALL} {brasileirao[-4:]}')
print(30 * '=-=')
print(f'{Fore.CYAN}Times em ordem alfabética:{Style.RESET_ALL} {sorted(brasileirao)}')
print(30 * '=-=')
print(f'{Fore.CYAN}A Chapecoense está na posição {Style.RESET_ALL}{Fore.GREEN} {brasileirao.index("Chapecoense") + 1}.')
