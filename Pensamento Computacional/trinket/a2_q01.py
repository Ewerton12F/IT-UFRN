"""
Questão 01
Francisco ingressou na universidade e em uma disciplina do primeiro semestre 
obteve 
nota N1 na primeira unidade, 
nota N2 na segunda unidade e 
nota N3 na terceira unidade. 

Ele não conhece bem as regras de pontuação e, portanto, precisa de ajuda para 
saber se está aprovado, reprovado ou em prova final nesta disciplina. 

A nota final de Francisco é calculada utilizando uma média ponderada na qual 
o peso da nota N1 é 2, 
o peso da nota N2 é 3 e 
o peso da nota N3 é 4. 

Caso a média final seja maior ou igual a 7, Francisco está aprovado. 
Caso a média seja menor que 3, Francisco está reprovado. 
Em caso contrário, terá que fazer a prova final. 

Para isso, faça um programa para imprimir qual é a situação de Francisco a 
partir de três notas informadas.

ENTRADA:
Qual é a nota da primeira unidade? 5.5
Qual é a nota da segunda unidade? 8.5
Qual é a nota da terceira unidade? 8.0
SAÍDA:
Francisco está aprovado
            
ENTRADA:
Qual é a nota da primeira unidade? 5.5
Qual é a nota da segunda unidade? 2.5
Qual é a nota da terceira unidade? 1.0
SAÍDA:
Francisco está reprovado
            
ENTRADA:
Qual é a nota da primeira unidade? 5.5
Qual é a nota da segunda unidade? 6.5
Qual é a nota da terceira unidade? 4.0
SAÍDA:
Francisco está em prova final
"""

N1 = float(input("Qual é a nota da primeira unidade? "))
N2 = float(input("Qual é a nota da segunda unidade? "))
N3 = float(input("Qual é a nota da terceira unidade? "))
N1 = N1 * 2
N2 = N2 * 3
N3 = N3 * 4
MF = (N1 + N2 + N3) / 9

if MF >= 7:
    print("Francisco está aprovado")
else:
    if MF < 3:
        print("Francisco está reprovado")
    else:
        print("Francisco está em prova final")