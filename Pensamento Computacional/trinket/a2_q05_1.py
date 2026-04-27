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
"""
import matplotlib.pyplot as plt
import numpy as np


l1 = int(input("Tamanho do lado do quadrado 1? "))
l2 = int(input("Tamanho do lado do quadrado 2? "))
l3 = int(input("Tamanho do lado do quadrado 3? "))
l4 = int(input("Tamanho do lado do quadrado 4? "))

quadrados = [l1, l2, l3, l4]
media_soma_l = (l1 + l2 + l3 + l4) / 4
inicio_quadrado_eixo_x = [
	0,
	l1 + media_soma_l,
	l1 + media_soma_l + l2 + media_soma_l,
	l1 + media_soma_l + l2 + media_soma_l + l3 + media_soma_l,
]
q_maior = quadrados[0]
q_menor = quadrados[0]

for i in quadrados:
	if i > q_maior:
		q_maior = i
	if i < q_menor:
		q_menor = i

for i in range(4):
	if quadrados[i] == q_maior:
		color = 'g'
	elif quadrados[i] == q_menor:
		color = 'r'
	else:
		color = 'k'

	inicio_x_x = 0 + inicio_quadrado_eixo_x[i] # início do comprimento do segmento de reta no eixo x 
	inicio_x_y = 0
	final_y_x = 0 + inicio_quadrado_eixo_x[i] + quadrados[i] # final do comprimento do segmento de reta no eixo x 
	final_y_y = 0
	q_xl_inferior = np.array([inicio_x_x, final_y_x])
	q_yl_inferior = np.array([inicio_x_y, final_y_y])

	inicio_x_x = 0 + inicio_quadrado_eixo_x[i] # início do comprimento do segmento de reta no eixo x 
	inicio_x_y = 0 + quadrados[i]
	final_y_x = 0 + inicio_quadrado_eixo_x[i] + quadrados[i] # final do comprimento do segmento de reta no eixo x
	final_y_y = 0 + quadrados[i]
	q_xl_topo = np.array([inicio_x_x, final_y_x])
	q_yl_topo = np.array([inicio_x_y, final_y_y])

	inicio_x_x = 0 + inicio_quadrado_eixo_x[i]
	inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
	final_y_x = 0 + inicio_quadrado_eixo_x[i]
	final_y_y = 0 + quadrados[i] # final do comprimento do segmento de reta no eixo y
	q_xl_esquerdo = np.array([inicio_x_x, final_y_x])
	q_yl_esquerdo = np.array([inicio_x_y, final_y_y])

	inicio_x_x = 0 + inicio_quadrado_eixo_x[i] + quadrados[i]
	inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
	final_y_x = 0 + inicio_quadrado_eixo_x[i] + quadrados[i]
	final_y_y = 0 + quadrados[i] # final do comprimento do segmento de reta no eixo y
	q_xl_direito = np.array([inicio_x_x, final_y_x])
	q_yl_direito = np.array([inicio_x_y, final_y_y])

	plt.plot(
		q_xl_inferior, 
		q_yl_inferior,
		q_xl_topo,
		q_yl_topo,
		q_xl_direito,
		q_yl_direito,
		q_xl_esquerdo, 
		q_yl_esquerdo, 
		color = color
	)
plt.show()