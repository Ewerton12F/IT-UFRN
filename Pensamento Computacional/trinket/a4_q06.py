"""
Questão 06
Imagine que você está ajudando a organizar um evento esportivo onde várias 
competições estão acontecendo simultaneamente, como corridas, saltos em altura, 
e arremesso de peso. Cada competição tem diversos participantes que registram 
diferentes pontuações ou distâncias. Para tornar a tarefa de registrar o recorde 
de cada competição mais eficiente e dinâmica, você decidiu desenvolver um 
algoritmo que permite aos juízes inserir as pontuações de cada atleta e 
automaticamente determinar o maior valor registrado, facilitando a identificação 
do recorde atual quase instantaneamente.

Você foi designado para desenvolver um algoritmo que auxilie os juízes de um 
evento esportivo a registrar e identificar os recordes de cada competição. O 
algoritmo deve permitir que os juízes continuem inserindo as pontuações 
alcançadas pelos atletas em uma competição específica até que um juiz digite o 
valor 0 (zero), que indica o término da entrada de dados para aquela competição. 
Após receber o sinal de término, o algoritmo deve analisar os valores fornecidos 
e exibir o maior deles, indicando o recorde atual da competição.

ENTRADA
Informe as pontuações dos atletas. Digite 0 para encerrar
10
2
2 
42
0
SAÍDA
O recorde de pontos é 42.
ENTRADA
Informe as pontuações dos atletas. Digite 0 para encerrar
13
22
120
10
13
120
0
O recorde de pontos é 120.
"""

recorde = 0
x = 1
pontuacoes = []
print("Informe as pontuações dos atletas. Digite 0 para encerrar")

while x != 0:
    x = int(input())
    pontuacoes.append(x)

for y in pontuacoes:
    if recorde < y:
        recorde = y

print(f"O recorde de pontos é {recorde}")