"""
Questão 01
Imagine que você foi convidado para fazer um trabalho voluntário trabalhando na 
equipe de pesquisa em saúde pública e vai ajudar a avaliar a eficácia de uma 
nova vacina testando-a em dez pacientes distintos (uma pesquisa real teria bem 
mais indivíduos, mas para fins de exercício, vamos considerar somente dez). Cada 
paciente recebe a vacina em diferentes condições e o pesquisador registra a taxa 
de um determinado exame que indica o sucesso da vacina. Para obter uma visão 
completa sobre o desempenho geral da vacina, o pesquisador opta por calcular 
três tipos de médias: aritmética, geométrica e harmônica. Essas médias oferecem 
perspectivas diferentes:

Média Aritmética: É a soma de todos os valores dividida pelo número de valores. 
É útil quando todos os dados são considerados igualmente importantes e não há 
valores extremos que possam distorcer a média.

 - (somatória de x valores) / x:
'''
for x in valores:
    somatoria = somatoria + valores[x]
somatoria / len(valores)
'''

Média Geométrica: É a raiz n-ésima do produto dos valores. Ela é particularmente 
sensível a valores extremos e é mais adequada para dados que seguem uma 
distribuição log-normal, frequentemente encontrada em estudos de crescimento ou 
taxas multiplicativas, como taxas de infecção.

- (produto de x valores) ** 2:
'''
for x in valores:
    produto = produto * valores[x]
produto ** (1 / len(valores))
'''

Média Harmônica: É o inverso da média média aritmética dos inversos dos valores. 
É apropriada para médias de razões ou velocidades, por exemplo, quando os dados 
representam taxas ou velocidades e são desproporcionalmente impactados por 
valores menores.

 - x valores / (somatória do inverso de x):

'''
for x in valores:
    somatoria = somatoria + (1 / valores[x])
len(valores) / somatoria 
'''
 
O pesquisador também calcula o erro médio comparando a média geométrica e a 
harmônica com a média aritmética, para entender as variações entre elas. Essas 
fórmulas podem ser encontradas aqui. Os erros são calculados da seguinte forma:

Erro_harmônica: (média harmônica - média aritmética) / média aritmética

Erro_geométrica: (média geométrica - média aritmética) / média aritmética

Erro_médio: (Erro_harmônica + Erro_geométrica) / 2

Ao usar essas médias juntas, o pesquisador pode obter uma visão robusta e 
diversificada do desempenho da vacina, identificando nuances que uma única média 
poderia ocultar.

Diante disso, elabore um programa que receba dez valores, representando as taxas 
registradas do exame e calcula e imprima o valor de cada tipo de média, bem como 
o erro médio. Observe o formato da saída nos exemplos.

ENTRADA:
Insira a taxa do exame para 10 pacientes:
1
2
3
4
5
6
7
8
9
10
SAÍDA
Média aritmética: 5.50
Média harmônica: 3.41
Média geométrica: 4.53
Erro médio: -27.79%

ENTRADA:
Insira a taxa do exame para 10 pacientes:
4
3
2
6
7
8
9
23
54
21
SAÍDA
Média aritmética: 13.70
Média harmônica: 5.75
Média geométrica: 8.47
Erro médio: -48.11%
"""

print("Insira a taxa do exame para 10 pacientes:")
valores = []

for x in range(10):
    valor = int(input())
    valores.append(valor)

somatoria = 0
for x in valores:
    somatoria = somatoria + x
media_aritmetica = somatoria / len(valores)
print(f"Média aritmética: {media_aritmetica:.2f}")

somatoria = 0
for x in valores:
    somatoria = somatoria + (1 / x)
media_harmonica = len(valores) / somatoria 
print(f"Média harmônica: {media_harmonica:.2f}")

produto = 1
for x in valores:
    produto = produto * x
media_geometrica = produto ** (1 / len(valores))
print(f"Média geométrica: {media_geometrica:.2f}")

Erro_harmonica = (media_harmonica - media_aritmetica) / media_aritmetica

Erro_geometrica = (media_geometrica - media_aritmetica) / media_aritmetica

Erro_medio = (Erro_harmonica + Erro_geometrica) / 2
print(f"Erro_medio {Erro_medio*100:.2f}")
