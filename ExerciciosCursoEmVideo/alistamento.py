print('-=-'*6)
print('\033[31mALISTAMENTO MILITAR\033[m')
print('-=-'*6)
from datetime import date
atual=date.today().year
sexo=str(input('Qual seu sexo?[Masculino/Feminimo] ')).lower()
if sexo == 'masculino':
    nascimento=int(input('Qual seu ano de nascimento: '))
    idade=atual-nascimento
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você precisa de alistar IMEDIATAMENTE!')
    elif idade < 18:
        tempo=18-idade
        print(f'Falta {tempo} anos para o alistamento')
        ano=atual+tempo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        tempo=idade-18
        print(f'Você ja deveria ter se alistado há {tempo} anos')
        ano=atual-tempo
        print(f'Seu alistamento foi em {ano}')
else:
    print('Você não precisa fazer o alistamento militar obrigatório.')