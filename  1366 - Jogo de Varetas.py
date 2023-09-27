# Jogo de Varetas

# Há muitos jogos divertidos que usam pequenas varetas coloridas. A variante usada neste problema envolve a construção de retângulos. O jogo consiste em, dado um conjunto de varetas de comprimentos variados, desenhar retângulos no chão, utilizando as varetas como lados dos retângulos, sendo que cada vareta pode ser utilizada em apenas um retângulo, e cada lado de um retângulo é formado por uma única vareta. Nesse jogo, duas crianças recebem dois conjuntos iguais de varetas. Ganha o jogo a criança que desenhar o maior número de retângulos com o conjunto de varetas.

# Dado um conjunto de varetas de comprimentos inteiros, você deve escrever um programa para determinar o maior número de retângulos que é possível desenhar.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro N que indica o número de diferentes comprimentos de varetas (1 ≤ N ≤ 1.000) no conjunto. Cada uma das N linhas seguintes contém dois números inteiros Ci e Vi , representando respectivamente um comprimento (1 ≤ Ci ≤ 10.000) e o número de varetas com esse comprimento (1 ≤ Vi ≤ 1.000). Cada comprimento de vareta aparece no máximo uma vez em um conjunto de teste (ou seja, os valores Ci são distintos). O ﬁnal da entrada é indicado por N = 0.

# Saída
# Para cada caso de teste da entrada seu programa deve produzir uma única linha na saída, contendo um número inteiro, indicando o número máximo de retângulos que podem ser formados com o conjunto de varetas dado.


# -*- coding: utf-8 -*-

''' IDEIA DA SOLUCAO

Sei que cada retângulo será formado por 2 pares de varetas, sendo que as varetas de um mesmo par devem possuir comprimento igual.
Mesmo  assim, varetas que pertencem a dois pares diferentes que formam o mesmo retângulo podem tem comprimentos diferentes.
Sabendo disso, posso contar a quantidade de pares de varetas de mesmo comprimento que existem na entrada. É fácil obter isso, pois a cada 
valor de c e v lidos, devo dividir o v em pares, ou seja, será o quociente da divisão de v por 2. Acumulo isso em uma única variável, que será o 
total de pares possíveis de serem formados com a entrada. Depois, basta lembrar que cada retângulo precisa de dois pares, ou seja, obtenho novamente
o quociente da divisão do total de pares de varetas por 2.

'''

while True:
    n = int(input())

    if n == 0:
        break
    
    qtdePares = 0
    for i in range(n):    
        c, v = input().split()
        c = int(c)
        v = int(v)
        
        #Para cada comprimento de vareta, descubro quantos pares existem e acumulo esse valor na variável qtdePares
        qtdePares += v // 2
    
    #Descubro aqui quantos pares de "pares de varetas" consigo formar, visto que preciso sempre de 2 pares de varetas para formar um retângulo
    print(qtdePares // 2)