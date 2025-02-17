# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

tupla_quatro_valores = tuple(int(input("Digite um número: ")) for _ in range(4))
print(f'Tupla com os quatro valores: {tupla_quatro_valores}')

if tupla_quatro_valores.count(9) == 1:
    print(f'O valor 9 apareceu {tupla_quatro_valores.count(9)} vez.')
else:
    print(f'O valor 9 apareceu {tupla_quatro_valores.count(9)} vezes.')

if 3 in tupla_quatro_valores:
    print(f'O primeiro valor 3 foi digitado na posição {tupla_quatro_valores.index(3) + 1}.')
else:
    print('O valor 3 não foi digitado.')

pares = ()
for num in tupla_quatro_valores:
    if num % 2 == 0:
        pares += (num,)
if pares != ():
    print(f'Os números pares digitados foram: {pares}.')
else:
    print('Não digitados números pares.')

    # Resolução dos pares com lista
# pares = [num for num in tupla_quatro_valores if num % 2 == 0]
# print(f'Os números pares são: {pares}.')

