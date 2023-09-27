# Maratona

# A maratona é talvez a prova mais desgastante entre as modalidades olímpicas: são quarenta e dois mil, cento e noventa e cinco metros de percurso. Por isso, os organizadores sempre posicionam vários postos de água ao longo do trajeto da prova, onde copos de água são distribuídos aos competidores.

# João Saci é um jovem atleta que tem boas chances de se tornar um maratonista de primeira linha. No entanto, João Saci descobriu que somente consegue terminar uma maratona se ingerir alguns copos de água durante o percurso. O Laboratório de Biomecânica da universidade local, através de experimentos, determinou que João Saci consegue percorrer exatamente mais dois mil metros após o instante em que ingere um copo de água. A distância que João Saci consegue percorrer após ingerir um copo de água é denominada de distância intermediária máxima. Assim, se a distância entre dois postos de água consecutivos no percurso da maratona for sempre menor ou igual do que a distância intermediária máxima de João Saci, ele consegue terminar a prova. Caso contrário ele não consegue terminar a prova.

# O Laboratório de Biomecânica quer agora realizar estudos similares com outros maratonistas, que têm valor de distâncias intermediárias máximas distintas, e precisa de sua ajuda.

# Sua tarefa é escrever um programa que, dada a posição dos postos de água ao longo do percurso, e a distância intermediária máxima de um atleta, determine se o atleta consegue ou não completar a prova.

# Entrada
# A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).

# A primeira linha da entrada contém dois números inteiros N e M, separados por um espaço em branco, indicando respectivamente o número de postos de água (2 ≤ N ≤ 10000) e a distância intermediária máxima de um atleta, em metros (1 ≤ M ≤ 42195). A segunda linha contém N números inteiros Pi, separados por um espaço em branco, representando a posição dos postos de água ao longo do trajeto da maratona. A posição de um posto de água é dada pela distância, em metros, do início do percurso até o posto de água (0 ≤ Pi ≤ 42195 para 1 ≤ i ≤ N). O primeiro posto de água está sempre localizado no ponto de partida (ou seja, P1 = 0) e todos os postos estão em posições distintas. Além disso, os postos de água são dados na ordem crescente de sua distância ao início do percurso.

# Note que a distância total da prova é a oficial para a maratona, ou seja, 42195 metros.

# Saída
# Seu programa deve imprimir, na saída padrão, uma única linha contendo o caractere ‘S’ se o atleta consegue terminar a prova, ou o caractere ‘N’ caso contrário.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, devemos verificar se existe um intervalo entre os postos cuja distância seja maior que a distância suportada
pela pessoa na maratona (m). Para fazer isso, basta para cada posto atual verificar sua distância com o posto anterior.
Se essa distância for maior que m, então a pessoa não consegue completar a maratona. Deve-se ao final saber também a distância
entre a chegada e o último posto. Se a pessoa consegue também percorrer essa distância sem problemas, então ela consegue
completar toda a maratona. Caso alguma distância entre postos for maior que m, então dizemos que a pessoa não consegue
completar a maratona.
'''

n, m = input().split()
n = int(n)
m = int(m)

postos = input().split() #Leio todos os postos e converto para inteiro
for i in range(n):
    postos[i] = int(postos[i]) 
    
consegue = True #Marco inicialmente que a pessoa consegue completar a maratona
for i in range(1,n):
    if postos[i] - postos[i-1] > m: #Verifico a distância entre todo posto i com seu antecessor i-1. Se a distância for maior que m, então anoto que a pessoa não consegue completar a maratona
        consegue = False
        break
if consegue and 42195 - postos[n-1] > m: #Verifico também a distância entre a chegada e o último posto. Se a distância for maior que m, marco também que a pessoa não consegue completar a maratona
    consegue = False

if consegue:
    print("S")
else:
    print("N")