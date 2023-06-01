total_produtos=total_compra=contador=produto_barato=0
barato=''
print(40*'=')
print('{:^40}'.format('LOJA DESCONTÃO'))
print(40*'=')
while True:
    produto=str(input('Nome do produto: '))
    preco=float(input('Preço: R$'))
    contador+=1
    total_compra+=preco
    if preco >= 1000:
        total_produtos+=1
    if contador == 1 or preco < produto_barato:
        produto_barato=preco
        barato=produto
    resposta=str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resposta not in 'S,N':
        resposta=str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'''\nO total da compra foi R${total_compra:.2f}.
Temos {total_produtos} custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${produto_barato}''')
    