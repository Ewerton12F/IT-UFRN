"""
Questão 05
Uma criança gosta bastante de jogar um jogo de sequência numérica que, a partir 
de um número do tipo inteiro escolhido, mostra na tela uma sequência incluindo 
os dois números anteriores, o número escolhido, e os dois números posteriores. 
Além disso, também mostra na tela a soma de todos os números. Portanto, faça um 
programa que apresenta o resultado da tela do jogo a partir de um número 
informado.

ENTRADA:
Qual é o número inteiro que deve ser utilizado para gerar a sequência? 5
SAÍDA
A sequência é a seguinte: 3 4 5 6 7 25

ENTRADA:
Qual é o número inteiro que deve ser utilizado para gerar a sequência? 23
SAÍDA
A sequência é a seguinte: 21 22 23 24 25 115
"""

numero = int(input("Qual é o número inteiro que deve ser utilizado para gerar a sequência? "))
numero_m1 = numero - 1
numero_m2 = numero - 2
numero_M1 = numero + 1
numero_M2 = numero + 2
total = numero_m2 + numero_m1 + numero + numero_M1 + numero_M2
print(f"A sequência é a seguinte: {numero_m2} {numero_m1} {numero} {numero_M1} {numero_M2} {total}")
