"""
Questão 03
O Desenvolvimento de Interfaces de Usuário, ou UI Design, é uma área crítica da 
ciência da computação que se concentra em projetar interfaces visuais eficazes e 
agradáveis para programas de software e aplicações web. O objetivo principal é 
melhorar a interação entre o usuário e o aplicativo, tornando-a intuitiva, 
eficiente e agradável. Isso envolve a escolha de elementos de design, como 
layouts, cores e tipos de fonte, além de desenvolver a funcionalidade que 
responde às ações do usuário de maneira previsível e útil.

Sabendo disso, você foi encarregado de criar uma funcionalidade essencial em um 
aplicativo de planejamento de eventos. O objetivo é permitir que os usuários, ao 
planejarem eventos corporativos ou pessoais, possam selecionar o mês desejado 
através de um número, facilitando a organização e visualização de eventos em 
diferentes períodos do ano, mas exibindo de uma maneira mais familiar para todas 
as pessoas.

O aplicativo deve conter uma lista com os nomes dos doze meses. Quando o usuário 
digita um número entre 1 e 12, o aplicativo exibe o mês correspondente, tornando 
a interface intuitiva e amigável. Caso o número inserido esteja fora deste 
intervalo, o sistema deve informar imediatamente ao usuário sobre o erro, 
exibindo a mensagem: "Erro: não existe mês de número X. Por favor, digite um 
número entre 1 e 12.", onde X é o número que o usuário digitou.

Essa tarefa não só melhora a usabilidade do aplicativo mas também garante uma 
experiência mais fluída e eficiente na organização de eventos.

ENTRADA
Qual o número do mês?
1
SAÍDA
O mês é janeiro
ENTRADA
Qual o número do mês?
20
SAÍDA
Erro: não existe mês de número 20! Por favor, digite um número entre 1 e 12.
"""

MESES = [
    "janeiro", "fevereiro", "março", 
    "abril", "maio", "junho", 
    "julho", "agosto", "setembro",
    "outubro", "novembro", "dezembro"
    ]

numero = int(input("Qual o número do mês? "))

if 1 <= numero <= 12:
    print(f"O mês é {MESES[numero-1]}")
else:
    print(f"Erro: não existe mês de número {numero}! Por favor, digite um número entre 1 e 12.")