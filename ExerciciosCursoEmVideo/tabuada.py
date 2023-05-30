print('\033[33m-------- TABUADA --------\033[m')
numero=int(input('Digite um numero para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{numero} X {c} = {numero*c}')
print("ACABOU")