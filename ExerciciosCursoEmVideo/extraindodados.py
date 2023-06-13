lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta not in 'S,N':
        resposta=str(input('Digite um dado válido [S/N]. Quer continuar? ')).strip().upper()[0]
    if resposta in 'N':
        break
print(30*'-=')
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O numero 5 está nesta lista.')
else:
    print('O numero 5 não está nesta lista.')
print(30*'-=')