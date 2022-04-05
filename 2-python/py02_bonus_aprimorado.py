"""
Modulo: Calcula Correção de Poupança

Author: Prof. Jefferson
"""


def calcula_saldo(saldo, taxa, nmeses):
    """Calcula o valor corrigido do saldo da poupança"""
    i = 0
    while i < nmeses:
        saldo = saldo + saldo*taxa
        i += 1

    return saldo

arg_saldo = float(input("Saldo Inicial: "))
arg_taxa = float(input("Taxa mensal:"))
arg_nmeses = int(input("Número de meses:"))

arg_saldo = calcula_saldo(arg_saldo, arg_taxa, arg_nmeses)

print(f"O saldo final após {arg_nmeses} é de {arg_saldo}")
