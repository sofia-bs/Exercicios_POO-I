# Perdido em Marte

# No filme "Perdido em Marte", o astronauta Mark Watney está presumidamente morto depois de ter sido apanhado numa tempestade, onde é deixado para trás enquanto o resto da equipe planejam evacuar o planeta e regressar à Terra. Watney encontra-se assim sozinho e abandonado, com algumas provisões e a sua sagacidade, destreza e espírito para sobreviver e encontrar uma maneira de enviar um sinal para casa, sabendo que mesmo que saibam que ele está vivo, é muito vaga a hipótese de um salvamento.

# Watner, ainda vivo, necessitava entrar em contato com a NASA para informar que ainda estava vido, porém no lugar onde estava não tinha um meio de comunicação com a Terra, foi então que ele lembrou da missão da Pathfinder. que a nave aterrou no Planeta Vermelho a 4 de Julho de 1997 e libertou um pequeno rover com seis rodas, chamado Sojourner, para estudar o terreno vizinho. A missão tinha a duração de umas poucas semanas mas acabou por durar quase três meses. A nave comunicou pela última vez com as equipas na Terra a 27 de Setembro. Ele analisando no mapa percebeu que o Pathfinder ficou próximo de sua "estação", então o mesmo pensou em usá-lo como comunicação.

# Porém a única comunicação que existia era uma câmera que rotacionava 360 graus em seu próprio eixo, para registrar fotos em Marte e mandar para a NASA, como a distância da Terra para Marte são de 55,76 milhões de km (Não é exato, pois depende da posição da rotação com a terra, como referência o SOL), uma mensagem que é enviado da terra para Marte dura um tempo de 30 minutos (tecnologia da época), hoje é menor, e acredite, a mensagem andava na velocidade da luz, quando se criar a Dobra(Star Trek) isso será tranquilo.

# Watner Teve uma ideia, como a Câmera gira 360 Graus, ele estabeleceu em cada ponto, equidistante, no círculo, um valor Hexadecimal, na qual a Câmera iria apontar o código desejado, numa fração de segundos, E Watner iria anotar e verificar a lestra correspondente na sua tabela ASCII, conforme a figura abaixo.

# 360

# Você foi selecionado para trabalhar na NASA e terá que ajudar Watner a sobreviver, faça um programa que converta em hexadecimal para caracter para traduzir a msensagem, as letras só serão de "a-z" 26 caracteres.

# Exemplo: n=3, depois teremos três duplas de hexadecimais "6F 6C 61", e se verificar na tabela as letras correspondentes a 6F =o, 6C=l e 61=a, transformando em "ola".

# Entrada
# Ele terá um número n (1<=n<=100) indicando o tamanho da palavra, e "n" vezes de duas casas hexadecimais, na qual significa uma letra.

# Veja o exemplo abaixo:

# Saída
# Somente a mensagem traduzida


# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Neste problema, teremos que converter um número em hexadecimal para decimal e depois obter seu correspondente caracter pela tabela ASCII
O problema é muito parecido com o problema 2874, leia primeiro a solução do problema 2874 para depois voltar a este problema.
Embora também podemos converter hexadecimal para decimal fazendo um algoritmo, também podemos utilizar o que o Python3 já possui pronto.
Neste caso, uma busca por "hexa to decimal python3" no Google já nos dá a resposta. A função int aceita que um segundo parâmetro
informe a base numérica que queremos converter uma string para um decimal.
'''

n = int(input())
hexas = input().split()

x = ""
for i in range(n):
    d = int(hexas[i], 16) #Simplesmente chamo a função int com o parâmetro 16 (do hexadecimal)
    x += chr(d) #Concateno o caracter correspondente na palavra resultado x

print(x) #Imprimo na tela