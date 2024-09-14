saldo = 1000
saque = 200
limite = 200

#and

print(saque >= limite and limite <= saque)
print(saque > saldo and saque > limite)

#or

print(saque >= limite or limite <= saque)
print(saque > saldo or saque > limite)

#not

contatinhos = []

print(not contatinhos)

contatinhos_2 = ["ciclano", "beltrato"]

print(not contatinhos_2)

print(not "")

print(not "aqui tem que dar falso, porque a string possui valor, então o contrario é falso")

#parenteses

saldo = 100
limite = 800
saque = 500
conta_especial = True

print ((saldo >= saque and saque >= limite) or (conta_especial and saque >= limite))