numero=[1,7,5,3,9]
numero[2]=3
print(numero)
numero.append(8)
print(numero)
numero.sort(reverse=True)
print(numero)
numero.insert(2,2)
print(numero)
numero.remove(2)
print(numero)
numero.pop()
print(numero)
if 4 in numero:
    numero.remove(4)
else:
    print('Não achei o numero 4.')

for valor in numero:
    print(f'{valor}...', end='')
print()
numeros=list()
for posicao in range (0,5):
    numeros.append(int(input('Digite um valor:')))
for posicao, valor in enumerate(numeros):
    print(f'Na posição {posicao} encontrei o valor {valor}')


