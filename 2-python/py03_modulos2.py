import poupanca as poup


arg_saldo = float(input("Saldo Inicial: "))
arg_taxa = float(input("Taxa mensal:"))
arg_nmeses = int(input("Número de meses:"))

arg_saldo = poup.calcula_saldo(arg_saldo, arg_taxa, arg_nmeses)

print(f"O saldo final após {arg_nmeses} é de {arg_saldo}")