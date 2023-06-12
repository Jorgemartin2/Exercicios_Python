contador='zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    numero=int(input('\nDigite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o numero {contador[numero]}')