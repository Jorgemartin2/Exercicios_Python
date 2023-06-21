matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=soma_3coluna=maior_2linha=0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para [{linha},{coluna}]: '))
print(30*'=')
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares+=matriz[linha][coluna]
    print()
for linha in range(0,3):
    soma_3coluna+=matriz[linha][2] 
for coluna in range(0,3):
    if coluna == 0:
        maior_2linha=matriz[1][coluna]
    elif matriz[1][coluna]>maior_2linha:
        maior_2linha=matriz[1][coluna] 
print(30*'=')
print(f'A soma dos numeros pares é {soma_pares}')
print(45*'-')
print(f'A soma dos valores da terceira coluna é {soma_3coluna}')
print(45*'-')
print(f'O maior valor da segunda linha é o numero {maior_2linha}')
print(45*'-')