soma=media=quantidade=maior=menor=0
resposta='S'
while resposta in 'S,s':
    numero=int(input('Digite um numero: '))
    soma+=numero
    quantidade+=1
    if quantidade == 1:
        maior=menor=numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta=str(input('Quer continuar?[S/N] ')).upper().strip()[0]
media=soma/quantidade
print(f'Você digitou {quantidade} numeros e a média entre eles é {media}')
print(f'O maior numero digitado é {maior} e o menor é {menor}')
