# Campo Minado

# Leonardo Viana é um garoto fascinado por jogos de tabuleiro. Nas férias de janeiro, ele aprendeu um jogo chamado "Campo minado", que é jogado em um tabuleiro comN células dispostas na horizontal. O objetivo desse jogo é determinar, para cada célula do tabuleiro, o número de minas explosivas nos arredores da mesma (que são a própria célula e as células imediatamente vizinhas à direita e à esquerda, caso essas existam). Por exemplo, a figura abaixo ilustra uma possível configuração de um tabuleiro com 5 células:



# A primeira célula não possui nenhuma mina explosiva, mas é vizinha de uma célula que possui uma mina explosiva. Nos arredores da segunda célula temos duas minas, e o mesmo acontece para a terceira e quarta células; a quinta célula só tem uma mina explosiva em seus arredores. A próxima figura ilustra a resposta para esse caso.



# Leonardo sabe que você participa da OBI e resolveu lhe pedir para escrever um programa de computador que, dado um tabuleiro, imprima o número de minas na vizinhança de cada posição. Assim, ele poderá conferir as centenas de tabuleiros que resolveu durante as férias.

# Entrada
# A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 50) indicando o número de células no tabuleiro. O tabuleiro é dado nas próximas N linhas. A i-ésima linha seguinte contém 0 se não existe mina na i-ésima célula do tabuleiro e 1 se existe uma mina na i-ésima célula do tabuleiro.

# Saída
# A saída é composta por N linhas. A i-ésima linha da saída contém o número de minas explosivas nos arredores da i-ésima célula do tabuleiro.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, posso imaginar o tabuleiro como um vetor, inicialmente preenchido com 0's. Depois,
para cada posição que vou lendo devo incrementar 1 na própria posição e na de seus vizinhos, marcando as bombas.
Por exemplo, se na posição 3 tem uma bomba, devo somar 1 na posição 3, na posição 2 e na posição 4. Deve-se
apenas fazer atenção aos limites do tabuleiro para evitar erros de acesso a posições que não existem.
'''

n = int(input())

minasMarcadas = [0] * n #Esse vetor é o que irá armazenar o resultado

for i in range(0,n): #Para cada posição do tabuleiro, vejo se ele possui uma mina ou não
    m = int(input())

    #Anoto quem são meu vizinho esquerdo e meu vizinho direito
    vizinhoEsquerdo = i-1
    vizinhoDireito = i+1
    
    minasMarcadas[i] += m #Se m for 1 irá somar 1, caso contrário irá somar 0
    if vizinhoEsquerdo >= 0: #Se o vizinho esquerdo estiver dentro do tabuleiro, marco ele
        minasMarcadas[vizinhoEsquerdo] += m #Se m for 1 irá somar 1, caso contrário irá somar 0
    if vizinhoDireito <= n-1: #Se o vizinho direiro estiver dentro do tabuleiro, marco ele
        minasMarcadas[vizinhoDireito] += m #Se m for 1 irá somar 1, caso contrário irá somar 0

for i in range(0,n):
    print("%d" % (minasMarcadas[i]))