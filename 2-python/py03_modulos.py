from poupanca import calcula_saldo

arg_saldo = 2000
arg_taxa = 0.01
arg_nmeses = 12

arg_saldo = calcula_saldo(arg_saldo, arg_taxa, arg_nmeses)

print(f"Testando a função de cálculo da poupança: Saldo após {arg_nmeses} é de {arg_saldo}")