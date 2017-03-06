# Faça um programa que determine os 100 primeiro termos da sequência de Fibonacci
n1, n2, count = 0, 1, 0
while count < 100:
    print(n2, end=' ')  # end = avoid the newline after the output
    n1, n2 = n2, n1+n2
    count += 1
