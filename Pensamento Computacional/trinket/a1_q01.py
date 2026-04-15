"""
Questão 1:
Uma turma de amigos vai fazer uma viagem para visitar a serra no período das 
festas juninas e está querendo saber quanto será necessário gastar de 
combustível para a realização da viagem. Para isso, eles verificam a distância 
da viagem de ida e volta em quilômetros, quantos quilômetros o carro percorre 
com cada litro de combustível e o preço em reais por litro de combustível. 
Com essas informações em mãos, faça um programa que calcule o valor total que 
eles gastarão em reais para realizar a viagem pretendida.

ENTRADA:
Qual é a distância da viagem de ida e volta em quilômetros? 200.0
Quantos quilômetros o carro percorre com cada litro de combustível? 10.0
Qual é o preço em reais por litro de combustível? 5.0
SAÍDA:
O valor em reais para realizar a viagem pretendida é 100.0

ENTRADA:
Qual é a distância da viagem de ida e volta em quilômetros? 550.0
Quantos quilômetros o carro percorre com cada litro de combustível? 7.5
Qual é o preço em reais por litro de combustível? 6.0
SAÍDA:
O valor em reais para realizar a viagem pretendida é 440.0
"""

distancia_km = float(input("Qual é a distância da viagem de ida e volta em quilômetros? "))
km_por_litro = float(input("Quantos quilômetros o carro percorre com cada litro de combustível? "))
preco_por_litro = float(input("Qual é o preço em reais por litro de combustível? "))
litros_necessarios = distancia_km / km_por_litro
custo_total = litros_necessarios * preco_por_litro
print(f"O valor em reais para realizar a viagem pretendida é {custo_total:.1f}")
