soma=0
contador=0
for c in range(1, 101):
    if c % 3 == 0:
        soma += c
        contador += 1
print (f'A soma dos {contador} valores solicitados é {soma}')