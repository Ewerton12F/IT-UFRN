"""
Enunciado

Você resolveu se aventurar no período de matrículas e, pelo alta concorrência nas
disciplinas do IMD, tentou cursar algo no curso de Engenharia Civil. Logo no
primeiro dia, o professor da disciplina adiantou que o projeto final vai ser a
construção de um projeto de ponte (que enrascada, hein?). Você ainda vai aprender
muita coisa para trabalhar no seu projeto, mas já conseguiu perceber que uma das
etapas críticas do projeto é a análise dos componentes estruturais para garantir
que eles formem triângulos adequados, já que triângulos são formas fundamentais
em estruturas devido à sua estabilidade. Usando os conceitos já das primeiras
aulas, sabe que vão ser usadas vigas para construção e que elas precisam formar
um triângulo para ajudar na sustentação da ponte.

Fazendo uso do seu conhecimento de programação, você decidiu automatizar o
processo de verificação das medidas das vigas. No seu algoritmo, você recebe as
medidas de três vigas que formarão um triângulo e precisa determinar a
configuração exata desse triângulo para planejar corretamente a estrutura da
ponte.

Ou seja, o seu algoritmo deve ler três valores reais A, B e C, representando os
comprimentos das vigas. Ordene-os em ordem decrescente, de modo que o lado A
represente o maior dos três lados. A seguir, determine o tipo de triângulo que
esses três lados formam, com base nos seguintes critérios, sempre escrevendo uma
mensagem adequada:

Se A ≥ B + C, apresente a mensagem: NAO FORMA TRIANGULO
Se A**2 = B**2 + C**2, apresente a mensagem: TRIANGULO RETANGULO
Se A**2 > B**2 + C**2, apresente a mensagem: TRIANGULO OBTUSANGULO
Se A**2 < B**2 + C**2, apresente a mensagem: TRIANGULO ACUTANGULO
Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

A entrada contém três valores de ponto flutuante de dupla precisão
A (0 < A), B (0 < B) e C (0 < C).
Imprima todas as classificações do triângulo especificado na entrada.
"""

A, B, C = sorted(map(float, input().split()), reverse=True)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
