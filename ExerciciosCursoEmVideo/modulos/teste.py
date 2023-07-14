from moeda import *

preco=float(input('Digite o preço: '))
print(f'A metade de {preco} é {metade(preco)}')
print(f'O dobro de {preco} é {dobro(preco)}')
print(f'Aumentando 10%, temos R${aumentar(preco, 10)}')
print(f'Diminuindo 5%, temos R${diminuir(preco, 5)}')