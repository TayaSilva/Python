print("-="*5, "CALCULADORA","-="*5)

cal = 0


n1 = int(input("Digite o primeiro valor para a conta: "))
n2 = int(input("Digite o segundo valor para a conta: "))
print("-="*5, "O QUE DESEJA FAZER","-="*5 ,"\n[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
while cal !=5:
    cal = int(input("Qual sua opção: "))

    if cal ==1:
        print("O resultado de {} + {} = {}".format(n1,n2,n1+n2))
    elif cal ==2:
        print("O resultado de {} X {} = {}".format(n1,n2,n1*n2))
    elif cal ==3:
        if n1 < n2:
            print("O numero {} é maior".format(n2))
        else:
            print("Entre {} e {} o numero {} é maior".format(n1,n2,n1))
    elif cal ==4:
        n1 = int(input("Digite o primeiro valor para a conta: "))
        n2 = int(input("Digite o segundo valor para a conta: "))
        print("-="*5, "O QUE DESEJA FAZER","-="*5 ,"\n[ 1 ] somar \n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    else:
        print("Numero invalido, tente novamente")



print("\033[1;36mCalculadora encerrada")







