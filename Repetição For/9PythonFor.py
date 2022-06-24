from datetime import date

contmenor = 0
contmaior =0
atual = date.today().year

for pess in range (1,8):

    nasc = int(input("Digite seu ano de nascimento: "))
    idade = atual - nasc

    if idade <18:
        contmenor +=1
    else:
         contmaior +=1

print("Tivemos {} pessoas maior de idade".format(contmaior))
print("Tivemos {} pessoas menor de idade".format(contmenor))