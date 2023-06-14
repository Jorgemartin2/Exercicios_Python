lista=[]
lista_pares=[]
lista_impares=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta=str(input('Quer adicionar mais um elemento? [S/N]')).strip().upper()[0]
    if resposta not in 'S,N':
        resposta=str(input('Digite um dado válido [S/N]. Quer adicionar mais um elemento?')).strip().upper()[0]
    if resposta in 'N':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print(20*'-=')
print(f'Lista completa: {lista} ')
print(f'Lista de numeros pares: {lista_pares}')
print(f'Lista de numeros impares: {lista_impares}')
