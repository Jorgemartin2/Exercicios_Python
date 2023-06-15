numeros=[[], []]
valor=0
for contador in range (1,7):
    valor=int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(20*'=-')
numeros[0].sort()
numeros[1].sort()
print(f'Lista dos numeros pares {numeros[0]}')
print(f'Lista dos numeros impares {numeros[1]}')
