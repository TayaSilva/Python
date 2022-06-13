import random


'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o
nome do escolhido.'''

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

lista = [a1,a2,a3,a4]

escolhido = random.choice(lista)

print("O aluno escolhido no sorteio foi {}".format(escolhido))