from datetime import datetime
dados={}
dados['nome']=str(input('Nome: '))
nascimento=int(input('Ano de nascimento: '))
dados['idade']=datetime.now().year-nascimento
dados['carteira']=int(input('Carteira De Trabalho [0 não tem]: '))
if dados['carteira']!=0:
    dados['contratação']=int(input('Ano de contratação: '))
    dados['salario']=float(input('Salário: R$'))
    dados['aposentadoria']=dados['idade']+((dados['contratação']+35)-datetime.now().year)
print('=-'*15)
for keys, values in dados.items():
    print(f'{keys}: {values}')