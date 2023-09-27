# Mergulho

# O recente terremoto em Nlogônia não chegou a afetar muito as edificações da capital, principal epicentro do abalo. Mas os cientistas detectaram que o principal dique de contenção teve um dano significativo na sua parte subterrânea que, se não for consertado rapidamente, pode causar o seu desmoronamento, com a consequente inundação de toda a capital.

# O conserto deve ser feito por mergulhadores, a uma grande profundidade, em condições extremamente difíceis e perigosas. Mas como é a sobrevivência da própria cidade que está em jogo, seus moradores acudiram em grande número como voluntários para essa perigosa missão.

# Como é tradicional em missões perigosas, cada mergulhador recebeu no início do mergulho uma pequena placa com um número de identificação. Ao terminar o mergulho, os voluntários devolviam a placa de identificação, colocando-a em um repositório.

# O dique voltou a ser seguro, mas aparentemente alguns voluntários não voltaram do mergulho. Você foi contratado para a penosa tarefa de, dadas as placas colocadas no repositório, determinar quais voluntários perderam a vida salvando a cidade.

# Entrada
# A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto de duas linhas. A primeira linha contém dois inteiros N e R ( 1 ≤ R ≤ N ≤ 104), indicando respectivamente o número de voluntários que mergulhou e o número de voluntários que retornou do mergulho. Os voluntários são identificados por números de 1 a N. A segunda linha da entrada contém R inteiros, indicando os voluntários que retornaram do mergulho (ao menos um voluntário retorna do mergulho).

# Saída
# Seu programa deve produzir uma única linha para cada caso de teste, contendo os identificadores dos voluntários que não retornaram do mergulho, na ordem crescente de suas identificações. Deixe um espaço em branco após cada identificador (note que isto significa que deve haver um espaço em branco também após o último identificador). Se todos os voluntários retornaram do mergulho, imprima apenas o caractere ‘*’ (asterisco).


# -*- coding: utf-8 -*-

''' IDEIA DA SOLUCAO

Tenho um vetor com o tamanho correspondente ao número de mergulhadores +1. O índice do vetor corresponde ao código 
do mergulhador e a ideia é indicar se o mergulhador ainda falta voltar ou já voltou, assim o vetor pode ser de booleanos (True e False).
Terei que marcar inicialmente que todos os mergulhadores faltam voltar e para cada mergulhador lido na entrada eu marco que ele já voltou, ou seja, não falta mais voltar.
Ao final, basta percorrer esse vetor novamente e imprimir cada mergulhador cuja posição do vetor indica que ele ainda falta voltar. Neste ponto, também
controlo se todos os mergulhadores voltaram ou não, assim, marco inicialmente que todos voltaram até encontrar algum que falta voltar. Dessa forma, 
sei quando devo imprimir um *

'''

#Crio o vetor uma única vez para todos os casos de teste
faltaVoltar = [None] * 10001 

while True:
    try:
        n, r = input().split()
        n = int(n)
        r = int(r)
        
        mergulhadores = input().split()
        
        #Marco que todos ainda faltam voltar
        for i in range(1, n+1):
            faltaVoltar[i] = True
        
        #Cada mergulhador que voltou, marco que ele não falta mais voltar
        for m in mergulhadores:
            faltaVoltar[int(m)] = False
        
        #Percorro todo o vetor para localizar os que ainda faltam voltar e imprimo conforme formato da saída, ou seja, com espaços entre cada código de mergulhador
        todosVoltaram = True
        for i in range(1, n+1):
            if faltaVoltar[i]:
                print("%d " % (i), end='')
                todosVoltaram = False #Se algum mergulhador não voltou, então anoto que não é verdade que todos voltaram
                
        if todosVoltaram:
            print("*")
        else:
            print("")
        
    except EOFError:
        break