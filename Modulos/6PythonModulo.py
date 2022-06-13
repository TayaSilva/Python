from random import shuffle

'''Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

'''Pode declarar como str (string)'''

a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")

lista = [a1,a2,a3,a4]
shuffle(lista)

print("A ordem de alunos será ")
print(lista)










