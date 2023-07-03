from random import randint
from time import sleep
contador=1
jogo={'Jogador 1': randint(1,6),
      'Jogador 2': randint(1,6),
      'Jogador 3': randint(1,6),
      'Jogador 4': randint(1,6)}
print('VALORES SORTEADOS:')
for keys, values in jogo.items():
    print(f'{keys} tirou {values} no dado.')
    sleep(1)
print('-='*30)
print(f'{"== RANKING DOS JOGADORES ==":^60}')
print('-='*30)
jogo2=dict(sorted(jogo.items(), key=lambda item:item[1], reverse=True))
for keys, values in jogo2.items():
    print(f'{contador}º lugar: {keys} com {values}.')
    contador+=1
    sleep(1)
