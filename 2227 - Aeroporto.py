# Aeroporto

# A crescente utilização do transporte aéreo preocupa os especialistas, que prevêem que o congestionamento em aeroportos poderá se tornar um grande problema no futuro. Os números atuais já são alarmantes: relatórios oficiais demonstram que na Europa, em junho de 2001, houve uma média de 7.000 atrasos de vôos por dia. Preocupada com a previsão dos seus especialistas em trá- fego aéreo, a Associação de Transporte Aéreo Internacional (ATAI) está começando um estudo para descobrir quais são os aeroportos onde o tráfego aéreo pode vir a ser mais problemático no futuro.

# Como programador recém contratado pela ATAI você foi encarregado de escrever um programa para determinar, a partir de uma listagem de aeroportos e vôos, qual aeroporto possui maior probabilidade de congestionamento no futuro. Como medida da probabilidade de congestionamento será utilizado neste estudo o número total de vôos que chegam ou que partem de cada aeroporto.

# Entrada
# A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de teste contém dois números inteiros A (0 ≤ A ≤ 100) e V (0 ≤ V ≤ 10000), que indicam respectivamente o número de aeroportos e o número de vôos. Os aeroportos são identificados por inteiros de 1 a A. As V linhas seguintes contêm cada uma a informação de um vôo, representada por um par de números inteiros positivos X e Y (1 ≤ X ≠ Y ≤ A), indicando que há um vôo do aeroporto X para o aeroporto Y. O final da entrada é indicado quando A = V = 0.

# Saída
# Para cada conjunto de teste da entrada seu programa deve produzir três linhas. A primeira linha identifica o conjunto de teste, no formato “Teste n”, onde n é numerado a partir de 1. A segunda linha deve conter o identificador do aeroporto que possui maior tráfego aéreo. Caso mais de um aeroporto possua este valor máximo, você deve listar todos estes aeroportos, em ordem crescente de identificação, e separados por pelo menos um espaço em branco. A terceira linha deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida rigorosamente.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, devo contar a quantidade de vôos em cada aeroporto (chegando ou saindo). Depois, devo descobrir qual a
quantidade máxima de vôos em algum aeroporto. Essa quantidade máxima servirá para poder percorrer todos os aeroportos e aí
sim imprimir todos os aeroportos que possuem essa quantidade máxima de vôos.
'''

voos = [None] * 101
t = 1
while True:
    a, v = input().split() #Leio o número de aeroportos e vôos
    a = int(a)
    v = int(v)
    
    if a == 0 and v == 0: 
        break
    
    for i in range(1,a+1): #Inicializo todos os aeroportos com 0 vôos, iniciando de 1 até a (inclusive)
        voos[i] = 0
        
    for i in range(v): #Para cada vôo lido
        x, y = input().split()
        x = int(x)
        y = int(y)
        
        voos[x] += 1 #Somo um no aeroporto x
        voos[y] += 1 #Somo um no aeroporto y
    
    maximoVoos = 0 #Descubro o máximo de vôos nos aeroportos
    for i in range(1,a+1):
        if voos[i] > maximoVoos:
            maximoVoos = voos[i]
            
    print("Teste %d" % (t))
    for i in range(1,a+1): #Imprimo todos os aeroportos que possuem aquele número máximo de vôos
        if voos[i] == maximoVoos:
                print("%d " % (i), end='')
    print() #Quebro a linha com os aeroportos
    print() #Imprimo mais uma linha em branco entre os casos de teste
            
    t += 1 #Para próximo teste