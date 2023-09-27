# Evitando Chuva

# Rafael odeia pegar chuva, e para evitá-la ele começou a usar um sistema de previsão do tempo. Neste sistema ele consegue prever se irá chover no horário em que ele vai para o trabalho e/ou no horário que ele volta do
# trabalho.

# Rafael também odeia carregar guarda-chuva quando não está chovendo. Para evitar isso, ele vai comprar vários guarda-chuvas e deixá-los guardados em casa e no escritório, e só vai usá-los quando estiver chovendo. Ou seja, se estiver chovendo na hora de ir para o trabalho, ele vai pegar um guarda-chuva que está em sua casa, usá-lo no caminho para o trabalho, e deixá-lo lá. De maneira semelhante, se estiver chovendo na hora de voltar para casa, ele vai pegar um guarda-chuva que está no escritório, usá-lo no caminho para casa, e deixá-lo lá.

# Dadas as previsões meteorológicas, descubra quantos guarda-chuvas Rafael deve comprar e guardar em casa e no escritório, de modo que ele nunca se molhe e nunca precise carregar o guarda-chuva quando não estiver chovendo.
 

# Entrada
# A primeira linha da entrada contém um inteiro N, indicando a quantidade de dias previstos pelo sistema meteorológico (1 <= N <= 1000).

# Em seguida haverá N linhas, cada uma contendo duas palavras SD e SN, indicando a previsão do tempo para a ida e para a volta do trabalho, respectivamente. Se a palavra for "sol" significa que neste horário fará sol, e se a palavra for "chuva" significa que neste horário irá chover.
 

# Saída
# Para cada caso de teste imprima uma linha contendo dois inteiros C e E, indicando quantos guarda-chuvas Rafael deve comprar e guardar em sua casa e escritório.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema é importante notar que devemos controlar duas coisas: a quantidade de guarda-chuvas já existentes em cada local
e a quantidade de guarda-chuvas a ser comprada em cada local. Por exemplo, se notamos que está chovendo quando estamos indo ao
trabalho, devemos primeiro verificar se já temos guarda-chuva em casa. Se sim, basta usar, decrementando a quantidade de guarda-chuvas
que mantenho "estocado" em casa e incrementando a quantidade de guarda-chuvas que mantenho estocada no trabalho. Caso não tenha
guarda-chuva em casa, então devo incrementar a quantidade de guarda-chuvas a ser comprada e mantida em casa e também incrementar
a quantidade de guarda-chuvas que mantenho estocada no trabalho. Faço a mesma coisa quando estiver chovendo e tiver saindo do trabalho
para ir para casa.
'''

n = int(input())

#Inicio a quantidade de guarda-chuvas em casa e no trabalho com 0
casa = 0
trabalho = 0

#Aqui anoto quando tenho que comprar um novo guarda-chuva, lembrando que apenas preciso comprar um novo quando preciso usar e não tenho no local
comprarCasa = 0
comprarTrabalho = 0
for _ in range(n):
    sd, sn = input().split()
    
    if sd == "chuva": #Se estiver chovendo na ida para o trabalho, preciso ter guarda-chuva em casa
        if casa > 0: #Se já tenho um guarda-chuva em casa, então basta usar
            casa -= 1
            trabalho += 1
        else: #Caso contrário, devo comprar um
            comprarCasa += 1
            trabalho += 1
    
    if sn == "chuva": #Se estiver chovendo na volta do trabalho, preciso ter um guarda-chuva no trabalho
        if trabalho > 0: #Se já tenho um guarda-chuva no trabalho, então basta usar
            trabalho -= 1
            casa += 1
        else: #Caso contrário, devo comprar um
            comprarTrabalho += 1
            casa += 1
            
print("%d %d" % (comprarCasa, comprarTrabalho))