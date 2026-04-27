"""
Questão 06
Desenvolva um programa que 
leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo, 
e em caso positivo, desenhe este triângulo.

ENTRADA:
Comprimento da primeira reta? 10
Comprimento da segunda reta? 20
Comprimento da terceira reta? 30
SAÍDA:    
Estas retas NÃO PODEM FORMAR um triângulo!

ENTRADA:
Comprimento da primeira reta? 40
Comprimento da segunda reta? 20
Comprimento da terceira reta? 50
SAÍDA:
image

arco cosseno de um cosseno == ângulo
cos(A) = 0.5
arccos(0.5) = 60°
180 - arccos[cos(a)]
cosseno - lei dos cossenos
"""

a = int(input("Comprimento da primeira reta? "))
b = int(input("Comprimento da segunda reta? "))
c = int(input("Comprimento da terceira reta? "))


if a < b + c and b < a + c and c < a + b:
    print("Estas retas PODEM FORMAR um triângulo!")
else:
    print("Estas retas NÃO PODEM FORMAR um triângulo!")