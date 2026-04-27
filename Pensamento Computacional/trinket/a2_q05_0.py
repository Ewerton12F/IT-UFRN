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
import matplotlib.pyplot as plt
import numpy as np

inicio = 0

q1_xl_inferior = np.array([0, 9])
q1_yl_inferior = np.array([0, 0])

q1_xl_topo = np.array([1, 9])
q1_yl_topo = np.array([10, 10])

q1_xl_esquerdo = np.array([0, 0])
q1_yl_esquerdo = np.array([0, 9])


q1_xl_direito = np.array([10, 10])
q1_yl_direito = np.array([1, 9])

q2_xl_topo = np.array([20, 30])
q2_yl_topo = np.array([10, 10])

q2_xl_direito = np.array([30, 30])
q2_yl_direito = np.array([10, 0])

q2_xl_inferior = np.array([30, 20])
q2_yl_inferior = np.array([0, 0])

q2_xl_esquerdo = np.array([20, 20])
q2_yl_esquerdo = np.array([0, 10])

plt.plot(
        q1_xl_inferior, 
        q1_yl_inferior,
        q1_xl_topo,
        q1_yl_topo,
        q1_xl_direito,
        q1_yl_direito,
        q1_xl_esquerdo, 
        q1_yl_esquerdo, 
        q2_xl_inferior, 
        q2_yl_inferior,
        q2_xl_topo,
        q2_yl_topo,
        q2_xl_direito,
        q2_yl_direito,
        q2_xl_esquerdo, 
        q2_yl_esquerdo, 
         )
plt.show()


# # QUADRADO 1

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l1 # final do comprimento do segmento de reta no eixo x 
# final_y_y = 0
# q1_xl_inferior = np.array([inicio_x_x, final_y_x])
# q1_yl_inferior = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0 + l1
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l1 # final do comprimento do segmento de reta no eixo x
# final_y_y = 0 + l1
# q1_xl_topo = np.array([inicio_x_x, final_y_x])
# q1_yl_topo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# final_y_y = 0 + l1 # final do comprimento do segmento de reta no eixo y
# q1_xl_esquerdo = np.array([inicio_x_x, final_y_x])
# q1_yl_esquerdo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l1
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l1
# final_y_y = 0 + l1 # final do comprimento do segmento de reta no eixo y
# q1_xl_direito = np.array([inicio_x_x, final_y_x])
# q1_yl_direito = np.array([inicio_x_y, final_y_y])

# # QUADRADO 2

# INICIO_DO_QUADRADO_EIXO_X = l1 + media_soma_l

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l2 # final do comprimento do segmento de reta no eixo x 
# final_y_y = 0
# q2_xl_inferior = np.array([inicio_x_x, final_y_x])
# q2_yl_inferior = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0 + l2
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l2 # final do comprimento do segmento de reta no eixo x
# final_y_y = 0 + l2
# q2_xl_topo = np.array([inicio_x_x, final_y_x])
# q2_yl_topo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# final_y_y = 0 + l2 # final do comprimento do segmento de reta no eixo y
# q2_xl_esquerdo = np.array([inicio_x_x, final_y_x])
# q2_yl_esquerdo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l2
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l2
# final_y_y = 0 + l2 # final do comprimento do segmento de reta no eixo y
# q2_xl_direito = np.array([inicio_x_x, final_y_x])
# q2_yl_direito = np.array([inicio_x_y, final_y_y])

# # QUADRADO 3

# INICIO_DO_QUADRADO_EIXO_X = l1 + media_soma_l + l2 + media_soma_l

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l3 # final do comprimento do segmento de reta no eixo x 
# final_y_y = 0
# q3_xl_inferior = np.array([inicio_x_x, final_y_x])
# q3_yl_inferior = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0 + l3
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l3 # final do comprimento do segmento de reta no eixo x
# final_y_y = 0 + l3
# q3_xl_topo = np.array([inicio_x_x, final_y_x])
# q3_yl_topo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# final_y_y = 0 + l3 # final do comprimento do segmento de reta no eixo y
# q3_xl_esquerdo = np.array([inicio_x_x, final_y_x])
# q3_yl_esquerdo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l3
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l3
# final_y_y = 0 + l3 # final do comprimento do segmento de reta no eixo y
# q3_xl_direito = np.array([inicio_x_x, final_y_x])
# q3_yl_direito = np.array([inicio_x_y, final_y_y])

# # QUADRADO 4

# INICIO_DO_QUADRADO_EIXO_X = l1 + media_soma_l + l2 + media_soma_l + l3 + media_soma_l

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l4 # final do comprimento do segmento de reta no eixo x 
# final_y_y = 0
# q4_xl_inferior = np.array([inicio_x_x, final_y_x])
# q4_yl_inferior = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X # início do comprimento do segmento de reta no eixo x 
# inicio_x_y = 0 + l4
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l4 # final do comprimento do segmento de reta no eixo x
# final_y_y = 0 + l4
# q4_xl_topo = np.array([inicio_x_x, final_y_x])
# q4_yl_topo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X
# final_y_y = 0 + l4 # final do comprimento do segmento de reta no eixo y
# q4_xl_esquerdo = np.array([inicio_x_x, final_y_x])
# q4_yl_esquerdo = np.array([inicio_x_y, final_y_y])

# inicio_x_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l4
# inicio_x_y = 0 # início do comprimento do segmento de reta no eixo y
# final_y_x = 0 + INICIO_DO_QUADRADO_EIXO_X + l4
# final_y_y = 0 + l4 # final do comprimento do segmento de reta no eixo y
# q4_xl_direito = np.array([inicio_x_x, final_y_x])
# q4_yl_direito = np.array([inicio_x_y, final_y_y])

# plt.plot(
#         q1_xl_inferior, 
#         q1_yl_inferior,
#         q1_xl_topo,
#         q1_yl_topo,
#         q1_xl_direito,
#         q1_yl_direito,
#         q1_xl_esquerdo, 
#         q1_yl_esquerdo, 
#         q2_xl_inferior, 
#         q2_yl_inferior,
#         q2_xl_topo,
#         q2_yl_topo,
#         q2_xl_direito,
#         q2_yl_direito,
#         q2_xl_esquerdo, 
#         q2_yl_esquerdo, 
#         q3_xl_inferior, 
#         q3_yl_inferior,
#         q3_xl_topo,
#         q3_yl_topo,
#         q3_xl_direito,
#         q3_yl_direito,
#         q3_xl_esquerdo, 
#         q3_yl_esquerdo, 
#         q4_xl_inferior, 
#         q4_yl_inferior,
#         q4_xl_topo,
#         q4_yl_topo,
#         q4_xl_direito,
#         q4_yl_direito,
#         q4_xl_esquerdo, 
#         q4_yl_esquerdo, 
#          )
# plt.show()