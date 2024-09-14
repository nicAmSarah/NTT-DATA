limite_por_saldo = 500
saldo = 2000.0
opcao = int(input("digite a opção: [1]- Sacar [2]-Vericar Limite [3]- Ver extrato"))

if opcao == 1:
    saque = float(input("informe o  valor que você quer sacar?"))
    if saque <= limite_por_saldo:
        print("saque no valor de " + saque + "feito com sucesso!")
    elif saque > saldo:
        print("Saque com o valor de " + saque + "não realizado devido saldo insuficiente" )
    else: saque > limite_por_saldo
    print("Seu saque não foi feito devido a falta de limite.")
    
elif opcao == 2:
    print("Seu limite atualmente é "+ limite_por_saldo)

elif opcao == 3:
    print("Seu extrato...")


#Roda ai Matheus
#if (saque>=limite_por_saldo) or (saque>=saldo):
#   print("Saque não permitido")