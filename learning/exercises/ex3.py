# Em um frigorífico existem 4 porcos.
# Cada porco possui um “crachá” que o identifica com seu número de identificação e o seu peso.
# Faça um sistema que calcule e imprima o número e o peso do porco mais magro e o número e o peso do porco mais gordo.

numeros = [50, 100, 12, 430]
pesos = [40.8, 15.3, 44.7, 60.0]
index_menor = 0
index_maior = 0
for i in range(len(pesos)):
    if pesos[i] < pesos[index_menor]:
        index_menor = i
    elif pesos[i] > pesos[index_maior]:
        index_maior = i
print('Menor peso\nPorco:',numeros[index_menor], '- Peso:', pesos[index_menor])
print()
print('Maior peso\nPorco:',numeros[index_maior], '- Peso:', pesos[index_maior])
