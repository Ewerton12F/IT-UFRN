"""
Questão 03
Imagine que você decidiu adentar no mundo da Bioinformática e logo ingressou 
como membro de um projeto de pesquisa sobre a diversidade genética em populações 
de organismos. Para modelar a diversidade genética, é essencial entender as 
combinações possíveis de sequências de DNA, que dependem diretamente do número 
de permutações possíveis de bases nitrogenadas (adenina, timina, citosina, 
guanina) em uma cadeia de DNA de determinado comprimento.

Você ficou encarregado de desenvolver uma ferramenta computacional que ajude 
outros pesquisadores a calcular rapidamente o número de combinações possíveis de 
sequências de DNA, com base no comprimento da sequência. Para isso, é necessário 
implementar um algoritmo que calcule o fatorial de um número inteiro.

O fatorial de um número n (denotado como n!) é o produto de todos os inteiros 
positivos até n. Por exemplo, se o comprimento da sequência de DNA é 5, então o 
número de combinações possíveis é $4^5$, pois cada posição pode ser ocupada por 
uma de quatro bases. Para simplificar o cálculo de grandes potências como esta, 
você decide calcular 5! como um passo intermediário para entender a manipulação 
de grandes números em seu algoritmo.

De fato, o fatorial de um número é crucial em várias áreas da matemática, 
incluindo estatística, combinações, permutações e probabilidade. Em termos de 
permutações, o fatorial de um número n representa o total de maneiras diferentes 
que n itens podem ser organizados em sequência. No contexto genético, isso se 
traduz no número de maneiras diferentes que as bases podem ser arranjadas para 
formar uma sequência de DNA de comprimento n, assumindo que cada posição na 
sequência pode ser ocupada por qualquer uma das quatro bases.

Diante disso, implemente um algoritmo que calcule o fatorial de um número dado 
inteiro positivo para ser usado no cálculo de combinações possíveis em 
sequências de DNA. Veja alguns exemplos de entrada e saída

ENTRADA
Digite um número:
0
SAÍDA
O número deve ser maior que 0.

ENTRADA
Digite um número:
4
SAÍDA
Resultado do fatorial: 24

ENTRADA
Digite um número:
5
SAÍDA
Resultado do fatorial: 120
"""

print("Digite um número:")
n = int(input())
f = 1

if n == 0:
    print("O número deve ser maior que 0.")
else:
    for x in range(n):
        f = f * (x + 1)
        print(f)
    print(f"Resultado do fatorial: {f}")    
