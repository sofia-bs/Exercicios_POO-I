# Frase Binária

# Jhin é um jovem que nasceu na geração em que os computadores já faziam parte da vida das pessoas. Assim como muitos de seus amigos, ele sabe utilizar muito bem as tecnologias atuais. Porém, ele não queria apenas saber utilizar, ele gostaria de saber como a computação funcionava. Após ter estudado um pouco da origem do computador, Jhin percebeu que o sistema de computação não é tão simples quanto parece ser. Em meio a algumas de suas pesquisas, ele percebeu que o computador utiliza um sistema binário ou de base dois, representados por zeros e uns (0 e 1). Jhin descobriu que podemos converter os números binários em números decimais e que podemos utilizar um valor decimal para equivaler a um caractere de acordo com a tabela ASCII.

# Jhin achou interessante a ideia de como o computador entende o que digitamos e resolveu desenvolver um tradutor em que ele entraria com valores em binário e o programa devolveria a frase equivalente ao código binário digitado. Jhin conseguiu desenvolver o programa, no entanto, ele desafiou você programador a resolver o mesmo problema.

# Entrada
# A entrada é composta por vários casos de teste. A primeira linha do caso de teste contém um número inteiro N (1<= N <= 100000), as N próximas linhas contêm uma String B (00000001 <= B <= 11111111). A entrada é finalizada com o fim do arquivo.

# Saída
# Para cada caso de teste seu programa, imprima uma única linha onde será apresentada uma frase contendo todos os caracteres relacionados ao seu caso de teste.


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Neste problema, temos duas partes principais: a primeira é converter um número binário em decimal e a
segunda em como converter esse valor decimal em um caracter seguindo a tabela ASCII. Digitando tabela ASCII no Google
é possível verificar que há sempre um valor decimal que é mapeado para um caracter, assim apenas devemos implementar
esse mapeamento ou usar algo pronto. Numa breve pesquisa usando o termo "ascii to char Python3" já é possível encontrar
duas funções úteis ord e chr que permitem converter caracteres ASCII em valores decimais e vice-versa. Podemos usar elas!
'''
while True:
    try:
        n = int(input())
        x = ""
        for _ in range(n):
            s = input().strip() #Leio o número binário como string, removendo espaços eventuais antes e depois
            
            multiplicador = 1 
            d = 0 #Inicio meu número decimal valendo 0
            for i in range(len(s)-1, -1, -1): #Trabalho com a string da direita para a esquerda, pois os pesos dos valores 1 são menores na direita
                if s[i] == '1': #Se meu dígito atual for 1, devo somar o multiplicador atual no meu número decimal
                    d += multiplicador
                
                multiplicador *= 2 #A cada deslocamento à esquerda devo aumentar meu multiplicador, pois seu peso será maior
            x += chr(d)

        print(x) #Agora sim pulo linha para ir ao próximo caso de teste
    except EOFError:
        break