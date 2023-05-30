numero=int(input('Digite um número: '))
total=0
for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[33m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {numero} foi divisível {total} vezes')
if total ==2:
    print('E por esse motivo ele é PRIMO!')
else:
    print('E por esse motivo ele NÃO É PRIMO!')