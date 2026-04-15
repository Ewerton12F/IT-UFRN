"""
Questão 04
Um funcionário de uma empresa, que é dedicado, competente e sempre busca se 
aprimorar em sua área, está se programando para poupar metade do seu salário 
mensalmente até acumular o valor necessário para comprar um automóvel novo. Por 
ser um dos funcionários mais dedicados da sua equipe, o seu chefe já confirmou 
que ele terá 5% de aumento no salário. Assim, faça um programa que calcule o 
número de meses que esse funcionário precisará esperar para poder ter dinheiro o 
suficiente para comprar o seu automóvel novo à vista. Para isso, informe o 
salário do mês inicial e o preço do automóvel a ser adquirido.

ENTRADA:
Qual é o salário mensal inicial? 5000.00
Qual é o preço do automóvel a ser adquirido? 80000.00
SAÍDA:
O funcionário terá que esperar 31 meses
            
ENTRADA:
Qual é o salário mensal inicial? 3500.00
Qual é o preço do automóvel a ser adquirido? 100000.00
SAÍDA:
O funcionário terá que esperar 55 meses
"""
import math
salario = float(input(""))
automovel = float(input(""))
valor = math.ceil(automovel / (salario + (salario*0.05))*2)
print(valor)