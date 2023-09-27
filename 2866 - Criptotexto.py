# Criptotexto

# César é um detetive que investiga uma série de roubos que acontecem em sua cidade. Em todo lugar que um crime acontece, a pessoa que cometeu tal crime deixa uma mensagem escrita, formada por letras maiúsculas e minúsculas. César conseguiu achar um padrão nestas mensagens e agora extrai um texto oculto em cada mensagem e pede a sua ajuda para tentar descobrir quem está cometendo tais crimes.

# Entrada
# A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro C (2 <= C <= 99) relativo ao número de casos de teste. Nas C linhas seguintes, haverá mensagens codificadas, todas com um mesmo padrão em relação ao exemplo abaixo.

# Saída
# Para cada caso de teste de entrada do seu programa, você deve imprimir o texto extraído da mensagem original.


# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    s = input()
    b = "" #Crio uma string vazia que usarei para adicionar cada letra que deve ser impressa na saída
    for x in range(len(s)-1,-1,-1): #Percorro a string a partir da última posição em direção à primeira posição
        if s[x].islower(): #Garanto que apenas caracteres letras minúsculas serão colocadas na string que será impressa como resultado
            b += s[x] #Concateno o que está em b com a letra armazenada em s[x]
    print(b)

''' 
MEU RACIOCÍNIO:
C = int(input())

for i in range (C):
    entrada = input()
    palavra = entrada.split()
    letras_minusculas = 
    resultado = ''.join(letras_minusculas)
    resultado_invertido = resultado[::-1]
    print(resultado_invertido)
'''