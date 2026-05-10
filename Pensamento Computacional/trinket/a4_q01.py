"""
Questão 01
Imagine que você está organizando um evento e tem uma 
lista de convidados confirmados: Daniel, Aluizio, Isabel, Teles e Eduardo. 
Durante a entrada do evento, os convidados devem confirmar sua presença. 
Para isso, eles dizem seu nome, e você precisa verificar se eles estão na lista 
de convidados confirmados para permitir o acesso. Como organizador, você quis 
garantir que só tenham as pessoas autorizadas dentro do evento e ficou 
responsável por verificar a entrada dos convidados na porta do local. Para 
facilitar, você deve desenvolver um pequeno protótipo que vai fazer essa 
verificação de forma automática. Esse sistema deve:

Inicialmente, imprimir todos os nomes dos convidados confirmados para 
verificação.
Solicitar ao usuário que digite um nome. Verificar se o nome digitado está na 
lista de convidados confirmados. Imprimir uma mensagem informando se o convidado 
pode entrar no evento ("Nome está na lista, acesso permitido!") ou se o nome não 
está na lista ("Nome não está na lista, acesso negado!").

ENTRADA
Qual nome você quer verificar?
Daniel
SAÍDA
A lista contém os seguintes nomes:
Daniel
Aluizio
Isabel
Teles
Eduardo
O nome Daniel está na lista, acesso permitido!

ENTRADA
Qual nome você quer verificar?
Apuena
SAÍDA
A lista contém os seguintes nomes:
Daniel
Aluizio
Isabel
Teles
Eduardo
O nome Apuena não está na lista, acesso negado!
"""

nomes = ["Daniel", "Aluizio", "Isabel", "Teles", "Eduardo"]
verificar = input("Qual nome você quer verificar? ")
print("A lista contém os seguintes nomes:")

for x in nomes:
    print(x)

if verificar in nomes:
    print(f"O nome {verificar} está na lista, acesso permitido!")
else:
    print(f"O nome {verificar} não está na lista, acesso negado!")