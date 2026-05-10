"""
Questão 05
Imagine que você está ajudando a organizar um evento comunitário focado na 
sustentabilidade e ficou responsável por criar jogos educativos sobre reciclagem 
e conservação ambiental. Em um dos jogos, as atividades envolvem os moradores 
entregando itens recicláveis para ganhar pontos. Você, então, precisa 
desenvolver um algoritmo que identifique alguns valores que dão bônus para os 
jogadores dependendo do número de itens recicláveis que eles entregam. Em 
princípio, eles não sabem quantos pontos extras vão ganhar, e você vai informar 
na hora da entrega dos itens.

Toda vez que alguém entregar seu produtos recicláveis, você conta a quantidade e 
insere no algoritmo. A pontuação inicial do morador é o número de itens que ele 
entregou. O bônus dado ao morador vai ser a mediana da lista de todos os números 
ímpares e múltiplos de três entre 0 e o número de itens entregue.

Para mostrar ao morador o seu bônus, você deve mostrar todos os números da lista 
criada, o valor que ele ganhou de bônus e a pontuação final. Note que com essa 
prática de bonificação, quanto mais itens a pessoa entregar, mais chances ela 
tem de ganhar o jogo.

ENTRADA
Informe a quantidade de itens recicláveis:
10
SAÍDA
Lista: 3,9
Bônus: 6 pontos
Pontuação final: 16
ENTRADA
Informe a quantidade de itens recicláveis:
20
SAÍDA
Lista: 3,9, 15
Bônus: 9 pontos
Pontuação final: 29
"""

itens = int(input("Informe a quantidade de itens recicláveis: "))
lista = []

if itens == 3:
    lista.append(itens)
else:
    for x in range(0, itens, 3):
        if x % 2 != 0:
            lista.append(x)

lista_exibir = str(lista)[1 : -1]
print(f"Lista: {lista_exibir}")

if len(lista) > 1:
    mediana = (lista[0] + lista[-1]) // 2
else:
    mediana = itens

print(f"Bônus: {mediana}")
final = itens + mediana
print(f"Pontuação final: {final}")