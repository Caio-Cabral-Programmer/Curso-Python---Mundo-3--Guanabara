# Tupla pode ser sem parênteses também.
# Tuplas são imutáveis. Comando errado: lanche [1] = 'Refrigerante'
# Tuplas são mais rápidas que listas.
# Tuplas são usadas para armazenar dados que não devem mudar.

tupla = 1, 2, 3, 4, 5
print (tupla)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print (lanche[cont])

print()

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print()

print(sorted(lanche))

print()

a = (2, 5, 4, 3,)
b = (5, 8, 1, 2, 3, 4)
c = a + b
d = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(d)

print()

pessoa = ('Gustavo', 39, 'M', 'Programador', 99.88)
print (pessoa)

print()

print (lanche)
print (lanche[0])
print (lanche[1])
print (lanche[2])
print (lanche[3])
print (lanche[-1])
print (lanche[-2])
print (lanche[-3])
print (lanche[-4])
print (lanche[1:3])
print (lanche[2:])
print (lanche[:3])
print (lanche[-3:-1])
print (lanche[-1::-1])
print (lanche[::-1])