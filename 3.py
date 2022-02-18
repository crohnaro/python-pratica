vel = int(input("Qual a velocidade do seu carro?"))

if vel > 110 :
    multa = (vel - 110)*5
    print ("O valor da multa é de:", multa)
else:
    print ("Seu carro nao tem multa")
