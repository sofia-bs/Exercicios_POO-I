# Abaixo da Diagonal Principal

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo (área verde).




# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.


# -*- coding: utf-8 -*-

o = input()

mat = [None] * 12 #Cria uma matriz 12x12
for i in range(0, 12):
    mat[i] = [None] * 12

for i in range(0, 12): #Lê os 144 elementos
    for j in range(0, 12):
        mat[i][j] = float(input())

soma = 0
quantidade = (144 - 12)/2 #Elementos no triângulo inferior
for i in range(0, 12): #Soma elementos no triângulo inferior
    for j in range(0,i):
        soma += mat[i][j]
    
if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/quantidade))