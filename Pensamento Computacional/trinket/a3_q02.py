"""
Questão 02
Imagine que você é um desenvolvedor de jogos trabalhando em um puzzle digital 
que desafia os jogadores a identificar padrões e simetrias. Um dos conceitos 
mais fascinantes que você decide incluir é o dos números palíndromos. Um número 
palíndromo é aquele que permanece o mesmo quando seus dígitos são lidos de trás 
para frente, assim como a palavra "radar" ou "osso".

Os números palíndromos podem ser utilizados de várias maneiras criativas em 
jogos, adicionando camadas de complexidade e desafio ou como parte da mecânica 
do jogo para criar uma experiência mais rica e envolvente para os jogadores. A 
seguir, destacam-se alguns cenários onde os números palíndromos poderiam ser 
integrados em jogos:

Quebra-cabeças e Enigmas: Em um jogo de aventura ou quebra-cabeça, números 
palíndromos podem ser usados como soluções para enigmas. Por exemplo, um enigma 
pode requerer que o jogador ajuste mecanismos antigos ou painéis de controle de 
modo que os números exibidos formem um palíndromo, para desbloquear uma porta 
secreta ou acessar um novo nível.
Sistema de Pontuação e Bônus: Em jogos que envolvem coleta de pontos ou moedas, 
alcançar um número palíndromo de pontos ou moedas pode ativar um bônus ou 
multiplicador de pontos. Isso incentiva os jogadores a planejar suas estratégias 
para atingir esses números específicos.
Jogos de Cartas ou Números: Em um jogo de cartas digital, certas combinações de 
cartas que resultam em números palíndromos podem ter poderes especiais ou 
desencadear eventos especiais no jogo, como uma jogada extra ou a capacidade de 
neutralizar um ataque do oponente.
Desafios Temporizados: Em jogos com elementos de tempo, como corridas ou jogos 
de fuga, parar o cronômetro em um tempo palíndromo (como 12:21 ou 13:31) pode 
resultar em recompensas extras ou desbloqueio de conquistas.
Códigos Secretos em RPGs: Em jogos de RPG, números palíndromos podem ser usados 
como códigos para acessar áreas secretas ou descriptografar mensagens 
importantes que são cruciais para a progressão da trama.
Jogos Educacionais: Para jogos com um foco educacional, resolver problemas que 
envolvem números palíndromos pode ajudar os jogadores (geralmente crianças) a 
melhorar suas habilidades matemáticas e de raciocínio lógico de uma maneira 
divertida e envolvente.
Elementos de Sorte e Probabilidade: Em jogos que envolvem sorte ou elementos de 
cassino, certos jogos podem ter jackpots ou prêmios especiais se os resultados 
de uma roleta, dados ou slots terminarem em um número palíndromo.
Diante desse cenário, faça um algoritmo que não apenas identifica se um número 
inserido é um palíndromo, mas também determina se é par ou ímpar. Esta 
habilidade poderá ser usada para adicionar uma camada extra de complexidade ao 
seu jogo, tornando-o ainda mais intrigante e desafiador para os jogadores. Veja 
alguns exemplos de entrada e saída.

ENTRADA
252
SAÍDA
252 é palíndromo e é par.

ENTRADA
12321
SAÍDA
12321 é palíndromo e é impar.

ENTRADA
123
SAÍDA
123 não é palíndromo mas é impar.
"""

numero = input()
inverso = ''

for x in range(len(numero)-1, -1, -1):
    inverso = inverso + str(numero[x])

if numero == inverso:
    saida = f"{numero} é palíndromo "
else:
    saida = f"{numero} não é palíndromo "

if int(numero) % 2 == 0:
    saida = saida + "e é par"
else:
    saida = saida + "mas é ímpar"

print(saida)
