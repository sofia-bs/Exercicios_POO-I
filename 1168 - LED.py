# LED

# João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

# Obs.: Para programadores de Javascript, recomenda-se o uso de "input.trim().split('\n')" para evitar erros conhecidos.

# (imagem de leds de 0 à 9)

# Entrada
# A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.

# Saída
# Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".


# -*- coding: utf-8 -*-

N = int(input())

for _ in range(N):
    valores = input().strip()
    leds = 0
    
    for digito in valores:
        if digito == '0':
            leds += 6
        elif digito == '1':
            leds += 2
        elif digito == '2':
            leds += 5
        elif digito == '3':
            leds += 5
        elif digito == '4':
            leds += 4
        elif digito == '5':
            leds += 5
        elif digito == '6':
            leds += 6
        elif digito == '7':
            leds += 3
        elif digito == '8':
            leds += 7
        else:
            leds += 6

    print("%d leds" % (leds))