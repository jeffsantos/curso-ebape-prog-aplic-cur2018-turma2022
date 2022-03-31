def calcula_saldo(saldo, taxa, nmeses):
    for i in range(nmeses):
        saldo = saldo + saldo*taxa
    return saldo

saldo = float(input("Saldo Inicial: "))
taxa = float(input("Taxa mensal:"))
nmeses = int(input("Número de meses:"))

saldo = calcula_saldo(saldo, taxa, nmeses)

print(f"O saldo final após {nmeses} é de {saldo}")