"""
Questão 04
Na área de Análise de Dados, sua tarefa é desenvolver um algoritmo que ajude em 
estudos demográficos ao calcular a média de idade de um grupo específico de 
pessoas. Este algoritmo será uma ferramenta útil para pesquisadores e analistas 
entenderem melhor a distribuição etária em diferentes coletividades ou eventos, 
podendo ser aplicado em contextos como pesquisas de mercado, estudos sociais ou 
planejamento urbano.

Sabendo que os únicos dados que o usuário possui são a quantidade de pessoas 
entrevistadas e a idade que cada uma informou, como você faria uma aplicação que 
pudesse medir a idade representativa para as pessoas daquele local? Observe por 
meio dos exemplos que a saída é apresentada em uma forma prática e acessível, 
especialmente útil para apresentações rápidas ou decisões baseadas em dados 
simplificados.

ENTRADA
Qual o número de pessoas? 
3
Informe as idades:
10
30
35
SAÍDA
A média de idade das pessoas é 25 anos
ENTRADA
Qual o número de pessoas? 
3
Informe as idades:
12
30
22
SAÍDA
A média de idade das pessoas é 21 anos
"""

numero_pessoas = int(input("Qual o número de pessoas? "))
print("Informe as idades:")
soma_idades = 0

for x in range(numero_pessoas):
    idade = int(input())
    soma_idades += idade

media = soma_idades // numero_pessoas

print(f"A média de idade das pessoas é {media} anos")