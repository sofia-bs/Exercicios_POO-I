# Matriz Quadrada I

# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e construa a matriz de acordo com o exemplo abaixo.

# Entrada
# A entrada consiste de vários inteiros, um valor por linha, correspondentes as ordens das matrizes a serem construídas. O final da entrada é marcado por um valor de ordem igual a zero (0).

# Saída
# Para cada inteiro da entrada imprima a matriz correspondente, de acordo com o exemplo. Os valores das matrizes devem ser formatados em um campo de tamanho 3 justificados à direita e separados por espaço. Após o último caractere de cada linha da matriz não deve haver espaços em branco. Após a impressão de cada matriz deve ser deixada uma linha em branco.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Neste problema, percebe-se que o padrão da matriz NxN diz que o valor de qualquer casa (i,j) é exatamente a menor distância da casa até a borda da matriz (sendo a distância mínima 1).
Dessa forma, podemos simplesmente calcular para cada casa (i,j), qual é esta distância. Note que a distância da borda superior é exatamente i+1, da borda inferior N-i, da borda esquerda j+1 e da borda direita N-j.
Obtendo todas essas distâncias devemos pegar o mínimo entre os 4 valores e basta. Fazemos isso para todas as casas da matriz.
'''

#Função para descobrir o mínimo entre 4 valores
def min(a,b,c,d):
    x = a
    if b < x:
        x = b
    if c < x:
        x = c
    if d < x:
        x = d
    return x

#Apenas declaro a matriz para usar ela em todos os casos de teste
mat = [None] * 100
for i in range(100):
    mat[i] = [None] * 100

while True:
    n = int(input())
    if n == 0: 
        break
        
    #Preencho a matriz usando a ideia da solução dita acima, computando a distância mínima de cada casa (i,j) em relação à borda da matriz
    for i in range(n):
        for j in range(n):
            mat[i][j] = min(i+1,j+1,n-i,n-j)

    #Apenas imprimo a matriz formatada
    for i in range(n):
        print("%3d" % mat[i][j], end='')
        for j in range(1, n):
            print(" %3d" % mat[i][j], end='')
        print()
    print()