"""
Enunciado:

Faça um programa que leia o valor de uma compra e a opção de pagamento
(V - para pagamento à vista ou
 P - para pagamento parcelado).
Caso o cliente pague à vista, terá um desconto de 5%, caso pague em 3 vezes terá
um acréscimo de 8%. O programa deve mostrar o valor da compra e o valor à vista
ou valor a prazo (valor total e o valor de cada parcela).
"""


def lervalor(valor: float, tipo_de_pag: str) -> None:
    if tipo_de_pag != "V":
        if tipo_de_pag != "P":
            while tipo_de_pag != "V" and tipo_de_pag != "P":
                tipo_de_pag = input("Opção inválida. Digite 'V' ou 'P': ")

    if tipo_de_pag == "V":
        valor_a_vista = valor * 0.95
        print(f"Valor a pagar: {valor_a_vista:.0f}")
    else:
        valor_parcelado = valor * 1.08
        valor_parcela = valor_parcelado / 3

        print(f"Valor a pagar: {valor_parcelado:.0f}")

        for x in range(1, 4):
            print(f"Parcela {x}: {valor_parcela:.0f}")


valor = float(input())
tipo_de_pag = input(
    "Digite 'V' para pagamento à vista ou 'P' para pagamento parcelado: "
)

lervalor(valor, tipo_de_pag)
