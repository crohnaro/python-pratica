"""Faça um programa que leia quatro notas, moestre as notas e a média na tela"""

notas = []
i = 1
while i <= 4:
    n = float(input("Digite suas notas:"))
    notas.append(n)
    i += 1
soma = 0
i = 0
while i <= 3:
    soma += notas[i]
    i += 1

print("Suas notas foram:", notas , "e sua média é:", (soma/i)) 
