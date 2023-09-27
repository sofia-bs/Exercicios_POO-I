# Deli Deli

# Sra. Deli está trabalhando em uma casa de mercearias finas "Deli Deli". No ano passado, a Sra. Deli decidiu expandir seu negócio e construir uma loja online. Ela contratou um programador que implementou a loja online.

# Recentemente alguns de seus novos clientes online reclamaram das notas fiscais eletrônicas. O programador esqueceu-se de usar o plural, no caso em que um item é comprado várias vezes. Infelizmente o programador da Sra. Deli está de férias e agora é sua tarefa de implementar esse recurso para a Sra. Deli. Aqui está uma descrição de como fazer o plural:

# Se a palavra está na lista de palavras irregulares substitua-a com o plural dado.
# Senão se a palavra termina em uma consoante seguida por "y", substitua "y" por "ies".
# Senão se a palavra termina em "o", "s", "ch", "sh" ou "x", acrescente "es" à palavra.
# Senão acrescente "s" à palavra.
# Entrada
# A primeira linha do arquivo de entrada consiste de dois inteiros L e N (0 ≤ L ≤ 20, 1 ≤ N ≤ 100). As seguintes L linhas contém a descrição das palavras irregulares e sua forma plural. Cada linha é composta de duas palavras separadas por um caractere de espaço, onde a primeira palavra é o singular, a segunda palavra é a forma plural de uma palavra irregular. Depois da lista de palavras irregulares, as N linhas seguintes contém uma palavra cada, que você tem que transformar para o plural. Você pode assumir que cada palavra é composta de no máximo 20 letras minúsculas do alfabeto Inglês ('a' a 'z').

# Saída
# Imprima N linhas na saída, onde a i-ésima linha é a forma plural da i-ésima palavra de entrada.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, primeiramente devemos armazenar as palavras irregulares e seu plural. Até essa aula não havíamos tido dicionários,
assim devemos armazenar em dois vetores (A e B), sendo que cada posição do vetor A indica uma palavra irregular e cada posição do 
vetor B indica o seu plural. Assim, por exemplo, a palavra rice estaria na posição 0 do vetor A e também na posição 0 do vetor B.
Ao imprimir a resposta, devemos primeiramente pesquisar nesse vetor A se a palavra encontra-se nele,
caso sim, imprimimos a correspondente do vetor B. Caso contrário, devemos aplicar as demais regras do
enunciado.
'''

l, n = input().split()
l = int(l)
n = int(n)

#Crio os dois vetores para armazenar as palavras irregulares e seus plurais
A = [None] * 21
B = [None] * 21

for i in range(0, l):
    A[i], B[i] = input().split() #Leio a palavra irregular e seu plural
    
for _ in range(0, n):
    palavra = input()
    
    #Pesquiso se a palavra existe no vetor A e imprimo seu plural
    acheiNoVetor = False
    for i in range(0,l):
        if A[i] == palavra:
            print(B[i]) #Se achar ela no vetor, já imprimo a saída
            acheiNoVetor = True
            break
            
    if not acheiNoVetor:
        t = len(palavra) #Calculo o tamanho da palavra para obter os último caracteres (poderia fazer isso usando valores negativos também)
        #Cada uma das condições abaixo trata as demais situações do plural, comparando o último ou dois últimos caracteres
        if t > 1 and palavra[t-1] == 'y' and not (palavra[t-2] == 'a' or palavra[t-2] == 'e' or palavra[t-2] == 'i' or palavra[t-2] == 'o' or palavra[t-2] == 'u') :
            print(palavra[0:t-1] + "ies")
        elif palavra[t-1] == 'o' or palavra[t-1] == 's' or palavra[t-1] == 'x':
            print(palavra + "es")
        elif t > 1 and palavra[t-1] == 'h' and (palavra[t-2] == 's' or palavra[t-2] == 'c'):
            print(palavra + "es")
        else:
            print(palavra + "s")