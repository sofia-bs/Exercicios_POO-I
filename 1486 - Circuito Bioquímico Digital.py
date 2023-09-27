# Circuito Bioquímico Digital

# Um circuito bioquímico digital (CBD) é um artefato composto de um conjunto de pontos de processamento. Cada ponto de processamento é constituído por um minúsculo receptáculo para reagentes bioquímicos, feito de um substrato biológico que se comporta como um microcircuito eletrônico digital. Dependendo do estado da reação no receptáculo, o substrato gera dois níveis de voltagem. Um leitor acoplado ao CBD é capaz de realizar a leitura de todos os pontos de processamento de um CDB num dado instante, interpretando os dois níveis de voltagem como 0 ou 1.

# Um experimento com o CBD é realizado da seguinte maneira. Os pontos de processamento são carregados com as substâncias de interesse e reagentes apropriados e, a cada intervalo fixo de tempo (tipicamente alguns milissegundos), os pontos de processamento são lidos. Assim, o experimento resulta em uma sequência de conjuntos (vetores) de bits, cada vetor correspondendo a uma medição do CBD.

# Uma sequência ininterrupta de bits 1 de um mesmo ponto de processamento ao longo do tempo é denominada de palito. O comprimento de um palito é o número de bits 1 que o compõe (note que o comprimento dos palitos de um experimento pode variar entre um e o número de medições efetuadas). Uma característica importante de um experimento com o CBD é a quantidade e o comprimento dos palitos gerados. A figura abaixo mostra o resultado de um experimento realizado com um CBD de seis pontos de processamento, em que foram efetuadas quatro medições, contendo três palitos de comprimento um, um palito de comprimento dois e um palito de comprimento quatro.



# Você foi contratado para escrever um programa que determine, dado o resultado de um experimento, quantos palitos de comprimento igual ou maior do que um certo valor foram gerados.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de um caso de teste contém três inteiros P, N e C que indicam respectivamente o número de pontos de processamento (1 ≤ P ≤ 1000), o número de medições efetuadas (1 ≤ N ≤ 1000) e o comprimento mínimo de palitos de interesse (1 ≤ C ≤ N). Cada uma das próximas N linhas contém sequências de P dígitos {0, 1}, separados por um espaço em branco. O final da entrada é indicado por P = N = C = 0.

# Saída
# Para cada caso de teste da entrada seu programa deve produzir uma única linha da saída, contendo o número de palitos de comprimento maior ou igual a C produzidos pelo experimento.


# -*- coding: utf-8 -*-
'''
Note que posso contar cada palito para cada ponto de processamento da seguinte forma:
1) Pegue um ponto de processamento qualquer e comece acumulando a quantidade de 1's até encontrar 0. Ao encontrar 0,
verifico se a quantidade de 1's que contei é maior que o tamanho de palito de interesse (c). O único detalhe
a cuidar é ao chegar na última linha de medição com um valor 1, assim, devo apenas verificar depois de computar a 
última linha o comprimento atual do palito, o qual pode ser diferente de 0 apenas se a última linha for 1 ou será 0
caso a última linha seja 0.
2) Aumento o problema para 'p' pontos de processamento, e então armazeno as quantidades de 1's para cada ponto de processamento
em um único vetor (chamado 'comprimentoPalito')
'''

#Utilizo este mesmo vetor para armazenar a quantidade de 1's para cada ponto de processamento
comprimentoPalito = [None] * 1001 

while True:
    p,n,c = input().split()
    p = int(p)
    n = int(n)
    c = int(c)
    
    if p == 0 and n == 0 and c == 0: 
        break

    #Acumulo a quantidade de palitos maiores que o interesse (c)
    maioresPalitos = 0
    for i in range(p): #Inicializo para cada ponto de processamento a quantidade de 1's 
        comprimentoPalito[i] = 0 
    
    for _ in range(n): #Para cada medição
        medicoes = input().split() #Leio uma medição para cada ponto de processamento
        for i in range(p):
            if medicoes[i] == '1': #Se a medição atual é 1 para o ponto de processamento i, então somo 1
                comprimentoPalito[i] += 1
            else: #Caso contrário, terminou a minha sequência de 1's e basta verificar se a quantidade de 1's somadas é maior que o interesse (c)
                if comprimentoPalito[i] >= c: #Se sim, somo 1 ao número de palitos maiores que c
                    maioresPalitos += 1  
                comprimentoPalito[i] = 0
    
    #Verifico depois da última medição se há palitos maiores que c formados, dado que a última linha poderia ainda terminar com 1's
    for i in range(p):
        if comprimentoPalito[i] >= c:
            maioresPalitos += 1
    
    #Apenas imprimo a resposta
    print(maioresPalitos)