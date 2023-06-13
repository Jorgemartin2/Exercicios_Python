lista=[]
for c in range (0,5):
    numero=int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Valor adicionado no final da lista...')
    else:
        posicao=0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Valor adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print(40*'=')
print(f'Os valores digitados em ordem foram {lista}')