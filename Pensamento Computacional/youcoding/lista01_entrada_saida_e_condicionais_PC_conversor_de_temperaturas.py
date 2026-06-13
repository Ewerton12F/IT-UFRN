"""
Enunciado

Imagine que você está planejando uma viagem para o Vale do Silício no final de
setembro. Você quer saber como as temperaturas locais podem variar em diferentes
escalas de temperatura para se preparar adequadamente. A previsão do tempo local
indica a temperatura em graus Fahrenheit, mas você também gostaria de saber como
essa temperatura seria em Celsius, já que é a sua habitual. Como também é curioso
com relação à diferentes escalas, por que não saber como ficaria o valor em Kelvin?

Ao pensar sobre o assunto, você pensou que seu problema deve ser o mesmo passado
por várias outras pessoas e decidiu que vai ajudar. Para isso, você precisa
escrever um algoritmo que permita ao usuário informar a temperatura (em números
reais) e a escala utilizada (Celsius, Fahrenheit ou Kelvin). A saída do programa
será a temperatura nas três escalas, com duas casas decimais de precisão. A
entrada é composta pelo valor da temperatura, seguida de uma letra que vai
indicar a escala em que ela está.
"""


def tratamento_de_resposta(valor_e_escala: str) -> tuple:
    valor = float(valor_e_escala[:-2])
    escala = valor_e_escala[-1]
    return (valor, escala)


def c_em_f(temp_c_para_f: float) -> float:
    return (temp_c_para_f * 1.8) + 32


def c_em_k(temp_c_para_k: float) -> float:
    return temp_c_para_k + 273.15


def f_em_c(temp_f_para_c: float) -> float:
    return (temp_f_para_c - 32) * (5/9)


def f_em_k(temp_f_para_k: float) -> float:
    return ((temp_f_para_k - 32) * (5/9)) + 273.15


def k_em_c(temp_k_para_c: float) -> float:
    return temp_k_para_c - 273.15


def k_em_f(temp_k_para_f: float) -> float:
    return (temp_k_para_f - 273.15) * (9/5) + 32


def conversor_de_temp(valor_e_escala: str) -> None:
    """Calcula a conversão de um valor de uma escala em outras duas escalas.

    Args:
        valor_e_escala (str): Valor e escala separados por 1 espaço

    Retorna:
        print(f"Temperatura em Celsius: {:.2f} C")
        print(f"Temperatura em Fahrenheit: {:.2f} F")
        print(f"Temperatura em Kelvin: {:.2f} K")
    """

    valor, escala = tratamento_de_resposta(valor_e_escala)

    if escala == "C":
        conversao_c_para_f = c_em_f(valor)
        conversao_c_para_k = c_em_k(valor)
        print(f"Temperatura em Celsius: {valor:.2f} C")
        print(f"Temperatura em Fahrenheit: {conversao_c_para_f:.2f} F")
        print(f"Temperatura em Kelvin: {conversao_c_para_k:.2f} K")

    if escala == "F":
        conversao_f_para_c = f_em_c(valor)
        conversao_f_para_k = f_em_k(valor)
        print(f"Temperatura em Celsius: {conversao_f_para_c:.2f} C")
        print(f"Temperatura em Fahrenheit: {valor:.2f} F")
        print(f"Temperatura em Kelvin: {conversao_f_para_k:.2f} K")

    if escala == "K":
        conversao_k_para_c = k_em_c(valor)
        conversao_k_para_f = k_em_f(valor)
        print(f"Temperatura em Celsius: {conversao_k_para_c:.2f} C")
        print(f"Temperatura em Fahrenheit: {conversao_k_para_f:.2f} F")
        print(f"Temperatura em Kelvin: {valor:.2f} K")


valor_e_escala = input()

conversor_de_temp(valor_e_escala)
