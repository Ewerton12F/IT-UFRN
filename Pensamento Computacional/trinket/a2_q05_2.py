"""
Questão 05
Escreva um programa para pedir ao usuário e ler o valor dos lados de 4 quadrados. 
O programa deve desenhar todos os 4 quadrados separados no eixo X e pintar de 
verde o maior quadrado e de vermelho o menor deles.

ENTRADA
Tamanho do lado do quadrado 1? 40
Tamanho do lado do quadrado 2? 20
Tamanho do lado do quadrado 3? 50
Tamanho do lado do quadrado 4? 30

SAÍDA     
image

l1 = int(input("Tamanho do lado do quadrado 1?"))
l2 = int(input("Tamanho do lado do quadrado 2?"))
l3 = int(input("Tamanho do lado do quadrado 3?"))
l4 = int(input("Tamanho do lado do quadrado 4?"))

"""
import turtle

l1 = float(input('Tamanho do lado do quadrado 1?'))
l2 = float(input('Tamanho do lado do quadrado 2?'))
l3 = float(input('Tamanho do lado do quadrado 3?'))
l4 = float(input('Tamanho do lado do quadrado 4?'))
quadrados = [l1, l2, l3, l4]
media_soma_l = ((l1 + l2) + (l3 + l4)) / 4
inicio_quadrado_eixo_x = [0, l1 + media_soma_l, (l1 + media_soma_l) + (l2 + media_soma_l), ((l1 + media_soma_l) + (l2 + media_soma_l)) + (l3 + media_soma_l)]
q_maior = quadrados[0]
q_menor = quadrados[0]
for quad in quadrados:
  if quad > q_maior:
    q_maior = quad
  elif quad < q_menor:
    q_menor = quad
for j in range(1, 5):
  turtle.goto(inicio_quadrado_eixo_x[int(j - 1)],0)
  turtle.pendown()
  if quadrados[int(j - 1)] == q_maior:
    turtle.color('#006600')
    turtle.begin_fill()
  elif quadrados[int(j - 1)] == q_menor:
    turtle.color('#ff0000')
    turtle.begin_fill()
  else:
    turtle.color('#000000')
  turtle.forward(quadrados[int(j - 1)])
  turtle.left(90)
  turtle.forward(quadrados[int(j - 1)])
  turtle.left(90)
  turtle.forward(quadrados[int(j - 1)])
  turtle.left(90)
  turtle.forward(quadrados[int(j - 1)])
  turtle.left(90)
  turtle.penup()
  turtle.end_fill()