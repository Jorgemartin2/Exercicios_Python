lista=('Caderno', 15.99,
       'Lapis', 1.99,
       'Borracha', 2,
       'Estojo', 25,
       'Transferidor', 5.98,
       'Compasso', 9.95,
       'Mochila', 120.5,
       'Canetas', 32,
       'Livros', 23.75)
soma_itens=0
print(38*'=')
print(f'{"LISTAGEM DE PREÇOS":^38}')
print(38*'=')
for posicao in range (0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]:.<30}', end='')
    else:
        print(f'R${lista[posicao]:>5.2f}')
        soma_itens+=lista[posicao]
print(38*'=')
print(f'TOTAL DA COMPRA: R${soma_itens:.2f}')