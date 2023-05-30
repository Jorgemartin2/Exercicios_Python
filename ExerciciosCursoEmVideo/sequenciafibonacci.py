print('='*30)
print('SEQUENCIA DE FIBONACCI')
print('='*30)
termos=int(input('Quantos termos voçê quer ver?'))
termo1=0
termo2=1
print('~'*30)
print(f'{termo1} -> {termo2}', end='')
contador=3
while contador <= termos:
    termo3=termo1+termo2
    print(f' -> {termo3}', end='')
    termo1=termo2
    termo2=termo3
    contador+=1
print(' -> FIM!')
print('~'*30)


