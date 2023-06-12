from time import sleep
numeros=[]
while True:
    valor=float(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não irei adicionar!')
    resposta=str(input('Quer continuar S/N ? ')).strip().upper()[0]
    if resposta not in 'S,N':
        resposta=str(input('Digite uma resposta válida. Quer continuar S/N ? '))
    if resposta in 'N':
        break
print(30*'=')
print('Criando uma lista...')
sleep(2)
print(30*'=')
numeros.sort()
print(f'Lista criada com os valores {numeros} que você adicionou.')