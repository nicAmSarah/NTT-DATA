saldo = 1000
saque = 2000

status = "Sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")