from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print("------ JÓKENPÔ ------")
print("Suas opções: \n"
      "[0] PEDRA \n"
      "[1] PAPEL \n"
      "[2] TESOURA")
jogador = int(input("Qual sua jogada? "))
print('JÓKENPÔ ...')
sleep(2)

print('-=' * 12)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)

if computador == 0:
      if jogador == 0:
            print('\033[1;34mEMPATE!!!')

      elif jogador == 1:
            print('\033[1;32mJogador VENCEU')

      elif jogador == 2:
            print('\033[1;31mComputador VENCEU')

      else:
            print('Opção invalida')

elif computador == 1:
      if jogador == 0:
            print('\033[1;31mComputador VENCEU')

      elif jogador == 1:
            print('\033[1;34mEMPATE!!!')

      elif jogador == 2:
            print('\033[1;32mJogador VENCEU')

      else:
            print('Opção invalida')
elif computador == 2:
      if jogador == 0:
            print('\033[1;31mComputador VENCEU')

      elif jogador == 1:
            print('\033[1;32mJogador VENCEU')

      elif jogador == 2:
            print('\033[1;34mEMPATE!!!')

      else:
            print('Opção invalida')


