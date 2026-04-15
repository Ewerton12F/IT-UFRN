"""
Questão 06
Monique é uma programadora muito comunicativa que tem uma página em uma rede 
social para fazer postagens sobre programação. Ela é apaixonada por tecnologia e 
adora compartilhar seu conhecimento com os outros. É carismática, extrovertida e 
sempre encontra maneiras criativas de se conectar com as pessoas ao seu redor. 
Isso está fazendo ficar famosa, o que está levando-a a se interessar em abrir a 
sua própria empresa de comunicação. Para isso, já está pensando no marketing que 
irá fazer para promover a sua futura empresa e, portanto, quer testar várias 
frases de impacto associadas a nomes de pessoas. Logo, faça um programa que 
recebe um nome e uma frase de impacto e imprime a concatenação dessas 
informações.

ENTRADA:
Qual é o nome a ser utilizado? “Iuri”
Qual é a frase de impacto? “tem um belo futuro, pois acredita na beleza dos seus sonhos”      
SAÍDA:
“Iuri tem um belo futuro, pois acredita na beleza dos seus sonhos”
            
ENTRADA:
Qual é o nome a ser utilizado? “Maria”
Qual é a frase de impacto? “representa a mudança que você deseja ver no mundo”
SAÍDA:
“Maria representa a mudança que você deseja ver no mundo”
"""
nome = input("Qual é o nome a ser utilizado? ")
frase = input("Qual é a frase de impacto? ")
print(f"{nome} {frase}")