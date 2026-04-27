"""
Questão 03
Faça um programa que receba 
o valor do salário de uma pessoa e 
o valor de um financiamento pretendido. 
Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, 
o algoritmo deverá escrever "Financiamento Concedido". 
Caso contrário, ele deverá escrever "Financiamento Negado". 
Independente de conceder ou não o financiamento, 
o algoritmo escreverá depois a frase "Obrigado por nos consultar".

ENTRADA
Qual o valor do seu salário? 5000
Qual o valor do financiamento? 2000
SAÍDA
Financiamento Concedido!
Obrigado por nos consultar
        
ENTRADA
Qual o valor do seu salário? 5000
Qual o valor do financiamento? 90000
SAÍDA
Financiamento Negado!
Obrigado por nos consultar
"""

salario = float(input("Qual o valor do seu salário? "))
financiamento = float(input("Qual o valor do financiamento? "))

if financiamento <= (5 * salario):
    print("Financiamento Concedido!")
else:
    print("Financiamento Negado!")

print("Obrigado por nos consultar")