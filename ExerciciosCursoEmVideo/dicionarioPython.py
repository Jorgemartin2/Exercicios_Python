aluno={}
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>=7:
    aluno['situacao']='Aprovado'
elif aluno['media']>5 and aluno['media']<7:
    aluno['situacao']='Recuperação' 
else:
    aluno['situacao']='Reprovado'
print(15*'=-')
for keys, values in aluno.items():
    print(f'- {keys} : {values}')
