"""
Questão 02

Você foi convidado para ser professor por um dia. Com sua experiência como 
discente, você percebeu que o professor dava pouco feedback para os discentes 
quanto ao desempenho da turma nas avaliações. Então, como primeira tarefa, você 
foi revisar os resultados de uma recente prova aplicada para uma turma de 10 
alunos. Para entender melhor o desempenho geral e destacar os alunos que 
superaram as expectativas, você decide utilizar um programa de computador. 
Esse programa calcula automaticamente a média da turma e 
deve mostrar a média e listar as notas dos alunos que estão acima dela, 
ajudando você a identificar quem se destacou na prova. Este procedimento ajuda 
na preparação de feedbacks personalizados e no planejamento de aulas de reforço 
para aqueles que precisam melhorar.

ENTRADA
Digite 10 números:
1
2
3
4
5
6
7
8
9
10
SAÍDA
A média é: 5.5
Os números acima da média são:
6
7
8
9
10

ENTRADA
Digite 10 números:
47
37
11
89
28
78
81
62
83
26
SAÍDA
A média é: 54.2
Os números acima da média são:
89
78
81
62
83
"""

print("Digite 10 números: ")
lista_notas = []
soma_notas = 0

for x in range(10):
    numero = int(input())
    lista_notas.append(numero)

for y in lista_notas:
    soma_notas += y

media = soma_notas / len(lista_notas)
print(f"A média é: {media}")
print("Os números acima da média são:")

for z in lista_notas:
    if z > media:
        print(z)
