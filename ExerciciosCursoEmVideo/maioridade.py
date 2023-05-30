from datetime import date
ano_atual=date.today().year
total_maior=0
total_menor=0
for c in range(1, 8):
    ano_nascimento=int(input(f'Digite o ano em que a {c}º pessoa nasceu: '))
    idade=ano_atual-ano_nascimento
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1
print(f'Temos {total_maior} pessoas maior de idade')
print(f'Temos {total_menor} pessoas menor de idade')