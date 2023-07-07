from time import sleep


def maior(*numeros):
    contador=maior=0
    print('='*30)
    print('Analisando os valores passados...')
    for valor in numeros:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        contador+=1
    print(f'\nForam informados {contador} valores ao todo.')
    print(f'O maior valor informado foi o {maior}')


maior(2,9,4,3,2,7)
maior(2,5,8,2)
maior(1,0,6)
maior(1,2)
maior(5)
maior()
