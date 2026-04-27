"""
Questão 02
Faça um programa que leia o valor de uma compra e a opção de pagamento 
(V - para pagamento à vista ou P - para pagamento parcelado). 
Caso o cliente pague à vista, terá um desconto de 5%, 
caso pague em 3 vezes terá um acréscimo de 8%. 
O programa deve mostrar o valor da compra e o valor à vista ou valor a prazo 
(valor total e o valor de cada parcela).

Exemplo 1
Qual o valor da compra? 500
Como gostaria de pagar à vista(V) ou à prazo (P)? V
Valor à pagar 475
            
Exemplo 2
Qual o valor da compra? 500
Como gostaria de pagar à vista(V) ou à prazo (P)? P
Valor à pagar: 540
Parcela 1: 180
Parcela 2: 180
Parcela 3: 180
"""

compra = float(input("Qual o valor da compra? "))
pagar = input("Como gostaria de pagar à vista(V) ou à prazo (P)? ")
if pagar == "V":
    valor = compra * 0.95
else:
    valor = compra * 1.08
    parcela = valor / 3
print(f"Valor à pagar: {valor}")
if pagar == "P":
    print(f"Parcela 1: {parcela}")
    print(f"Parcela 2: {parcela}")
    print(f"Parcela 3: {parcela}")