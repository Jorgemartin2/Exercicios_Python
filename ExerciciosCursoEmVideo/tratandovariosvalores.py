numero=soma=contador=0
while True:
    numero=int(input('Digite um numero [999 para finalizar]: '))
    if numero == 999:
        break
    soma+=numero
    contador+=1
print(f'''PROGRAMA FINALIZADO!
Você digitou {contador} numeros e a soma deles é {soma}''')
