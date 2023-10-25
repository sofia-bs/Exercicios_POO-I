# Competição

# A maioria dos programadores que chegam a escrever competições com exercícios de programação concordam em quatro características que toda competição deve alcançar. Embora nem todas sejam sempre alcançadas, quanto mais melhor. As características são as seguintes:

# Ninguém resolveu todos os problemas.
# Todo problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).
# Não há nenhum problema resolvido por todos.
# Todos resolveram ao menos um problema (não necessariamente o mesmo).
# Rafael organizou uma competição alguns dias atrás, e está preocupado com quantas dessas características ele conseguiu alcançar com a competição.

# Dadas as informações sobre a competição, com o número de participantes, número de problemas, e qual participante resolveu quais problemas, descubra o número de características que foram alcançadas nesta competição.

# Entrada
# Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros N e M (3 ≤ N, M ≤ 100), indicando, respectivamente, o número de participantes e o número de problemas.

# Em seguida, haverá N linhas com M inteiros cada, onde o inteiro da linha i e coluna j é 1 caso o competidor i resolveu o problema j, ou 0 caso contrário.

# O último caso de teste é indicado quando N = M = 0, o qual não deverá ser processado.

# Saída
# Para cada caso de teste, imprima uma linha contendo um inteiro, representando quantas das características citadas foram alcançadas na competição.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Esse problema devo avaliar se a matriz obedece certas condições. Como há 4 condições para serem avaliadas podemos agrupar
em condições relativos aos problemas e condições relativas aos times. Como cada linha traz um time, fica fácil avaliar cada time
individualmente. Outra coisa que devemos notar é que devemos armazenar a quantidade de soluções corretas para cada problema, pois
apenas no final conseguiremos verificar as condições se todos os times resolveram um determinado problema ou se todos os problemas
foram resolvidos.
'''

solucoesProblemas = [None] * 101
while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if n == 0 and m == 0:
        break
        
    for i in range(m):
        solucoesProblemas[i] = 0 #Anoto a quantidade de times que resolveu cada problema, inicialmente com 0


    #Marco todos os critérios como verdadeiros até que depois consiga marcar algum como falso
    ngnResolveuTodos = True
    aoMenosUmProblema = True
    todoProblemaResolvido = True
    naoResolvidoPorTodos = True
    
    for i in range(n):
        solucoes = input().split()
        
        qtdeResolvidosTime = 0
        for j in range(m):
            if solucoes[j] == '1':
                qtdeResolvidosTime += 1 #Aumento a quantidade de problemas resolvidos pelo time i
                solucoesProblemas[j] += 1 #Aumento a quantidade de soluções para o problema j
        
        if qtdeResolvidosTime == m: #Se a quantidade de problemas resolvidos pelo time for igual ao total de problemas
            ngnResolveuTodos = False
            
        if qtdeResolvidosTime == 0: #Se o time não resolveu nada
            aoMenosUmProblema = False
    

    for i in range(m):
        if solucoesProblemas[i] == 0: #Se ninguém resolveu o problema i
            todoProblemaResolvido = False
        if solucoesProblemas[i] == n: #Se todos resolveram o problema i
            naoResolvidoPorTodos = False
    
    #Apenas somo 1 a cada critério satisfeito
    criteriosSatisfeitos = 0
    if ngnResolveuTodos:
        criteriosSatisfeitos += 1
    if aoMenosUmProblema:
        criteriosSatisfeitos += 1
    if todoProblemaResolvido:
        criteriosSatisfeitos += 1
    if naoResolvidoPorTodos:
        criteriosSatisfeitos += 1
    
    print(criteriosSatisfeitos)