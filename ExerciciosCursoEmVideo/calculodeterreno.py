def area(a,b):
    calculoArea=a*b
    print(f'A área de um terreno {a}x{b} é de {calculoArea}M²')


print('CÁLCULO DE TERRENOS')
print('-------------------')
largura=float(input('LARGURA (M): '))
comprimento=float(input('COMPRIMENTO (m): '))
area(largura,comprimento)