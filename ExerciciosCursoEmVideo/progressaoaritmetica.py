print('========== GERADOR DE P.A ==========')
primeiro_termo=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro_termo
contador=1
soma_termos=0
total=0
mais_termos=10
while mais_termos != 0:
    total+=mais_termos
    while contador <= total:
        print(f'{termo} - ', end='')
        termo+=razao
        contador+=1
    print('PAUSADO')
    mais_termos=int(input('Quantos termos voçê quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados na tela.')

