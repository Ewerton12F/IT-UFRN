"""
Questão 03
Um corretor de imóveis estava vendendo lotes de tamanhos variados para a 
construção de casas residenciais em um novo loteamento. O local era cercado por 
colinas verdejantes e um lago que cortava a paisagem. Em um determinado dia, 
apareceu um senhor que se mostrou interessado em comprar alguns lotes para 
construir a sua nova casa, a ser feita com materiais sustentáveis e projetada 
para se integrar perfeitamente ao ambiente natural da paisagem ao seu redor. Mas 
para poder tomar uma decisão de compra, solicitou ao corretor para calcular a 
área total de 4 lotes vizinhos que ele gostou em uma bela região do loteamento 
a fim de ter certeza que o espaço seria suficiente para criar um verdadeiro 
santuário natural. Com isso, faça um programa que calcule a área total (m2) do 
terreno contendo os 4 lotes. Para isso, informe a largura e o comprimento de 
cada um dos lotes.

ENTRADA:
Qual é a largura do lote 1? 25.0
Qual é o comprimento do lote 1? 50.0
Qual é a largura do lote 2? 30.0
Qual é o comprimento do lote 2? 70.0
Qual é a largura do lote 3? 25.0
Qual é o comprimento do lote 3? 50.0
Qual é a largura do lote 4? 50.0
Qual é o comprimento do lote 4? 100.0
SAÍDA:
A área total do terreno é 9600.0 m2
            
ENTRADA:
Qual é a largura do lote 1? 15.0
Qual é o comprimento do lote 1? 50.0
Qual é a largura do lote 2? 15.0
Qual é o comprimento do lote 2? 50.0
Qual é a largura do lote 3? 25.0
Qual é o comprimento do lote 3? 100.0
Qual é a largura do lote 4? 25.0
Qual é o comprimento do lote 4? 100.0      
SAÍDA:
A área total do terreno é 6500.0 m2
"""

l_lote1 = float(input("Qual é a largura do lote 1? "))
c_lote1 = float(input("Qual é o comprimento do lote 1? "))
l_lote2 = float(input("Qual é a largura do lote 2? "))
c_lote2 = float(input("Qual é o comprimento do lote 2? "))
l_lote3 = float(input("Qual é a largura do lote 3? "))
c_lote3 = float(input("Qual é o comprimento do lote 3? "))
l_lote4 = float(input("Qual é a largura do lote 4? "))
c_lote4 = float(input("Qual é o comprimento do lote 4? "))
area = (l_lote1*c_lote1)+(l_lote2*c_lote2)+(l_lote3*c_lote3)+(l_lote4*c_lote4)

print(f"A área total do terreno é {area} m2")