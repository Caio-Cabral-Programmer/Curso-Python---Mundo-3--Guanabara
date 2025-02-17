# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

def main():
    """
    Coleta 4 números do usuário e analisa:
    - Frequência do número 9
    - Posição do primeiro número 3
    - Números pares encontrados
    """
    # Coleta os números usando list comprehension
    numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))

    # Análise dos números
    qtd_nove = numeros.count(9)
    numeros_pares = tuple(num for num in numeros if num % 2 == 0)

    # Exibição dos resultados
    print(f"\nNúmeros digitados: {numeros}")

    # Verifica quantidade de noves
    print(f"O valor 9 apareceu {qtd_nove} {'vez' if qtd_nove == 1 else 'vezes'}")

    # Verifica posição do número 3
    try:
        posicao_tres = numeros.index(3) + 1
        print(f"O primeiro valor 3 está na {posicao_tres}ª posição")
    except ValueError:
        print("O valor 3 não foi digitado")

    # Verifica números pares
    if numeros_pares:
        print(f"Números pares digitados: {numeros_pares}")
    else:
        print("Nenhum número par foi digitado")

if __name__ == "__main__":
    main()
