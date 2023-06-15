pessoas=[]
dados=[]
maior_peso=menor_peso=0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas)==0:
        maior_peso=menor_peso=dados[1]
    else:
        if dados[1]>maior_peso:
            maior_peso=dados[1]
        if dados[1]<menor_peso:
            menor_peso=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta=str(input('Quer cadastrar mais alguém? [S/N]')).strip().upper()[0]
    if resposta not in 'S,N':
        resposta=str(input('Digite um dado válido [S/N]. Quer cadastrar mais alguém? '))
    if resposta in 'N':
        break
print(35*'=')
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso foi de {maior_peso} KG. O peso de ', end='')
for pessoa in pessoas:
    if pessoa[1]==maior_peso:      
        print(f'{pessoa[0]}.', end='')   
print(f'\nO menor peso foi de {menor_peso} KG. O peso de ', end='')
for pessoa in pessoas:
    if pessoa[1]==menor_peso:
        print(f'{pessoa[0]}.', end='')
        