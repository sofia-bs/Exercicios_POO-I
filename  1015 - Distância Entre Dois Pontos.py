# Distância Entre Dois Pontos

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

# Distancia = (imagem da fórmula da distância entre dois pontos)

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.


# -*- coding: utf-8 -*-

a, b = input().split()
c, d = input().split()
a = float (a)
b = float (b)
c = float (c)
d = float (d)
s = ((c-a)**2 + (d-b)**2)**0.5

print ("%.4f" % (s))