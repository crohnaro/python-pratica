minuto = float(input("Digite o valor dos minutos utilizados"))

if minuto < 200 :
    conta = minuto*0.20
    print ("O valor da conta é de: R$", conta)
elif minuto <= 400 :
    conta = minuto*0.18
    print ("O valor da conta é de: R$", conta)
elif minuto <= 800 :
    conta = minuto*0.15
    print ("O valor da conta é de: R$", conta)
else :
    conta = minuto*0.08
    print ("O valor da conta é de: R$", conta)
