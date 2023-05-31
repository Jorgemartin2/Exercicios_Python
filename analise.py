total_maior=total_homens=total_mulheres=0
resposta='S'
while resposta == 'S':
    print(30*'-')
    print('     CADASTRE UMA PESSOA')
    print(30*'-')
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'M,F':
        sexo=str(input('Digite um dado válido. Sexo [M/F]: ')).strip().upper()[0]
    resposta=str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resposta not in 'S/N':
        resposta=str(input('Digite um dado válido. Quer continuar [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        total_maior+=1
    if sexo == 'M':
        total_homens+=1
    if sexo == 'F' and idade < 20:
        total_mulheres+=1
print(f'''\nRESULTADO: 
Ao todo temos {total_maior} pessoas maiores de 18 anos.
Ao todo temos {total_homens} homens cadastrados.
Ao todo temos {total_mulheres} mulheres com menos de 20 anos.''')