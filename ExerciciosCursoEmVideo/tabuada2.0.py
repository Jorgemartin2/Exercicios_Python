print('========== TABUADA 2.0 ==========')
while True:
    numero=int(input('Quer ver a tabuada de qual numero?'))
    if numero < 0:
        break
    print('=='*17)
    for c in range(0, 11):
        print(f'{numero} X {c} = {numero*c}')
    print('=='*17)
print('PROGRAMA ENCERRAD0! Te esperamos em breve.')