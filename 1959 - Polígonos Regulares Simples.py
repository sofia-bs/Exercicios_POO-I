# Polígonos Regulares Simples

# Na geometria Euclidiana, um polígono regular é um polígono em que todos os ângulos são iguais e todos os lados tem o mesmo comprimento. Um polígono simples é aquele cujos segmentos de reta não se interceptam. Abaixo pode-se ver vários mosaicos feitos por polígonos regulares.

# (imagem de mosaicos feitos por polígonos regulares)

# Você deve escrever um programa que, dados o número e o comprimento dos lados de um polígono regular, mostre seu perímetro.

# Entrada
# A entrada tem dois inteiros positivos: N e L, que são, respectivamente, o número de lados e o comprimento de cada lado de um polígono regular (3 ≤ N ≤ 1000000 and 1 ≤ L ≤ 4000).

# Saída
# A saída é o perímetro P do polígono regular em uma única linha.


# -*- coding: utf-8 -*-

l, c = input().split()
l = int (l)
c = int (c)
p = l*c

print ("%d" % (p))