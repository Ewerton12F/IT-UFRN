"""
Questão 04
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado, e qual será o valor da multa. 
A multa vai custar R$7,00 por cada Km acima do limite.

Exemplo de entrada e saída:

Exemplo 1	
Qual é a velocidade atual do carro? 80
Tenha um bom dia! Dirija com segurança!
            
Exemplo 2
Qual é a velocidade atual do carro? 140
MULTADO! Você excedeu o limite permitido que é de 80Km/h!
Você deve pagar uma multa de R$ 420
"""

velocidade = int(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h!")
    print(f"Você deve pagar uma multa de R$ {multa}")
else:
    print("Tenha um bom dia! Dirija com segurança!")