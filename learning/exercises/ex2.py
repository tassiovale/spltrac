# Faça um programa que imprima o fatorial de um número
numero = 50
fatorial = 1
if numero > 0:
    for cont in range(1, numero+1):
        fatorial *= cont
    print('Fatorial de', numero, ':', fatorial)
else:
    print('Não é possível calcular o fatorial')
