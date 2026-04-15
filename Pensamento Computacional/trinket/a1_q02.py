"""
Questão 02
Você fez uma viagem super legal com os seus amigos e agora quer organizar outras 
viagens com o mesmo pessoal para explorar outras regiões. Só que, desta vez, irá 
utilizar um sistema de GPS no carro para facilitar o deslocamento em regiões 
desconhecidas, pois tiveram algumas dificuldades na última viagem, inclusive 
recebendo duas multas de trânsito por trafegar em ruas proibidas. Além disso, só 
perceberam que deveriam pagar as multas de trânsito com alguns dias após ter 
passado o prazo de pagamento, o que está fazendo o Detran acrescer o valor 
original com uma cobrança de juros. Portanto, faça um programa que calcule o 
valor das despesas para cada um dos amigos, dividindo igualmente o valor das 
multas de trânsito acrescidas de juros. Para isso, indique:
1. o valor original de cada multa de trânsito; 
2. a porcentagem de juros que o Detran está cobrado por atraso no pagamento e; 
3. a quantidade de amigos que contribuirão com as despesas.

ENTRADA:
Qual é o valor original cobrado por cada multa? 293.47
Qual é a porcentagem de juros cobrada pelo Detran? 3.0
Quantos amigos irão contribuir com as despesas? 5
SAÍDA:    
O valor em reais que cada amigo deverá pagar ao Detran é 120.91
            
ENTRADA:
Qual é o valor original cobrado por cada multa? 195.23
Qual é a porcentagem de juros cobrada pelo Detran? 5.0
Quantos amigos irão contribuir com as despesas? 4
SAÍDA:    
O valor em reais que cada amigo deverá pagar ao Detran é 102.49
"""

multa = float(input("Qual é o valor original cobrado por cada multa? "))
juros = float(input("Qual é a porcentagem de juros cobrada pelo Detran? "))
num_amigos = int(input("Quantos amigos irão contribuir com as despesas? "))
valor_final = ((multa + (multa * (juros / 100))) / num_amigos) * 2
print(f"O valor em reais que cada amigo deverá pagar ao Detran é {valor_final:.2f}")

