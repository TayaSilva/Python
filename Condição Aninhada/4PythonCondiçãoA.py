from datetime import date

print("Programa de maior idade para alistamento")
print("--------------------------------------------------------------")

sex = int(input("Qual o seu sexo? Digite [1] para feiminino e [2] para masculino: "))

if sex ==1:
    print("Você não precisa se alistar")
elif sex ==2:
    ano = int(input("Digite o seu ano de nascimento: "))
    data = date.today().year
    idade = data - ano


    print("Quem nasceu em {} hoje tem {} anos ".format(ano,idade))
    if idade < 18:
        falta = 18 - idade
        print("Fica tranquilo guerreiro, ainda não está na hora, falta {} ano(s)".format(falta))
        alis = data + falta
        print("Você vai se alistar no ano de {}".format(alis))
    elif idade ==18:
        print("\033[1;34mEstá na hora de se alistar!!!")
    elif idade >18:
        falta = idade - 18
        print("\033[1;31mJÁ PASSOU {} ANOS DA HORA DE SE ALISTAR!!!".format(falta))
        alis = data - falta
        print("O ano que você deveria ter se alistado era {}".format(alis))
else:
    print("\033[1;31mNumero invalido, tente novamente!")
