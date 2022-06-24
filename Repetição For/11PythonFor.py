somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
#-------------------------------------------

for c in range(1,4):
    print("-=-=-=-=-=- {}ª PESSOA -=-=-=-=-=-".format(c))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [M] ou [F]")).strip()

    somaidade += idade
# -------------------------------------------
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
#-------------------------------------------

    if idade < 20 and sexo in 'Ff':
        totmulher +=1





mediaidade = somaidade/4
print("A media de idade do grupo é {}".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho))
print("Temos {} mulher(es) com menos de 20 anos".format(totmulher))





