# Botas Perdidas

# A divisão de Suprimentos de Botas e Calçados do Exército comprou um grande número de pares de botas de vários tamanhos para seus soldados. No entanto, por uma falha de empacotamento da fábrica contratada, nem todas as caixas entregues continham um par de botas correto, com duas botas do mesmo tamanho, uma para cada pé. O sargento mandou que os recrutas retirassem todas as botas de todas as caixas para reembalá-las, desta vez corretamente.

# Quando o sargento descobriu que você sabia programar, ele solicitou com a gentileza habitual que você escrevesse um programa que, dada a lista contendo a descrição de cada bota entregue, determina quantos pares corretos de botas poderão ser formados no total.

# Entrada
# A entrada é composta por diversos casos de teste e termina com final de arquivo (EOF). A primeira linha de um caso de teste contém um inteiro N (2 ≤ N ≤ 10 4), N é par, indicando o número de botas individuais entregues. Cada uma das N linhas seguintes descreve uma bota, contendo um número inteiro M (30 ≤ M ≤ 60) e uma letra L, separados por uma espaço em branco. M indica o número da bota e L indica o pé da bota: L = 'D' indica que a bota é para o pé direito, L = 'E' indica que a bota é para o pé esquerdo.

# Saída
# Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número total de pares corretos que podem ser formados.


# -*- coding: utf-8 -*-

''' IDEIA DA SOLUCAO

Neste problema, preciso contar a quantidade de botas par direito e esquerdo possuo, para cada tamanho. Note que sempre que possuo alguma quantidade
de botas de certo tamanho, a quantidade de pares que consigo formar com aquele tamanho é o mínimo entre o par esquerdo e direito.
Assim, basta ler a entrada e acumular para cada tamanho a quantidade botas de cada lado, por isso preciso utilizar dois vetores, onde
o índice do vetor indica o tamanho da bota, enquanto que o valor que será atribuído naquele índice indica a quantidade de botas.
Ao final, basta percorrer ambos os vetores (esquerdo e direito), para cada tamanho, e descobrir o mínimo entre os dois. Esse mínimo
será a quantidade de pares com aquele tamanho e simplesmente devo acumular isso em alguma variável que indicará a quantidade total
de pares de botas.

'''

#Uso esses mesmos dois vetores para todos os casos de teste
direito = [None] * 61
esquerdo = [None] * 61

while True:
    try:
        
        n = int(input())
        
        #Como o tamanho vai apenas de 30 até 60, então apenas zero a quantidade de botas de ambos os lados neste intervalo de tamanho
        for i in range(30, 61):
            direito[i] = 0
            esquerdo[i] = 0
        
        #Para cada bota lida da entrada, ou somo ela no lado direito ou no lado esquerdo
        for i in range(n):
            m, l = input().split()
            if l == 'D':
                direito[int(m)] += 1
            else:
                esquerdo[int(m)] += 1
        
        #Percorro o vetor direito e esquerdo sempre buscando o mínimo entre os dois para cada tamanho e acumulo ele na variável qtdePares
        qtdePares = 0
        for i in range(30, 61):
            if direito[i] < esquerdo[i]:
                qtdePares += direito[i]
            else:
                qtdePares += esquerdo[i]
        
        print(qtdePares)
    except EOFError:
        break