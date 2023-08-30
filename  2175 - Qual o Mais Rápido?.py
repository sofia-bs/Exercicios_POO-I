# Qual o Mais Rápido?


# Otavio, Bruno e Ian são amigos de infância, apaixonados por desafios e esportes aquáticos. Em época de olimpíadas eles desafiam uns aos outros, simulando algumas competições, como a natação. O problema é que na natação, por exemplo, eles treinam bastante juntos e algumas vezes a diferença de tempo entre eles é muito curta, devido a isso, na maioria dos casos eles ficam horas e horas discutindo quem venceu. Agora eles resolveram investir no desenvolvimento de um equipamento eletrônico a ser utilizado especificamente na natação, que identifica o tempo que cada um nadou e exibe quem foi o mais rápido. Você faz parte da equipe que desenvolverá o equipamento e sua tarefa no projeto é criar um programa para receber o tempo dos 3 amigos e informar quem foi o vencedor.

# Entrada
# Cada caso de teste consiste em uma única linha contendo três números, separados por um espaço em branco, O (0 ≤ O ≤ 100), B (0 ≤ B ≤ 100) e I (0 ≤ I ≤ 100), representando respectivamente os tempos em segundos de Otavio, Bruno e Ian. Os tempos terão no máximo 3 casas decimais.

# Saída
# Para cada caso de teste, seu programa deverá imprimir uma única linha, contendo o nome do competidor vencedor, ou seja, o mais rápido. Caso haja empate e não for possível determinar um único vencedor, deverá imprimir a palavra “Empate”, sem aspas.


# -*- coding: utf-8 -*-

o, b, i = input().split()
o = float (o)
b = float (b)
i = float (i)

if o < b and o < i:
    print ("Otavio")

elif b < o and b < i:
    print ("Bruno")

elif i < o and i < b:
    print ("Ian")

else:
    print ("Empate")