numeros=[]
maior=0
menor=0
for posicao in range (0,5):
    numeros.append(int(input(f'Digite um valor para a posição {posicao}: ')))
    if posicao == 0:
        maior=menor=numeros[posicao]
    else:
        if numeros[posicao]>maior:
            maior=numeros[posicao]
        if numeros[posicao]<menor:
            menor=numeros[posicao]
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi o numero {maior} nas posições ', end='')
for indice,valor in enumerate(numeros):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor digitado foi o numero {menor} nas posições ', end='')
for indice,valor in enumerate(numeros):
    if valor == menor:
        print(f'{indice}...', end='')
