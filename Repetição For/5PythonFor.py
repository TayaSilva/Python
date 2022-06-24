cont = 0
soma= 0
for num in range (1,7):
    num = int(input("Digite o {}° valor:  ".format(num)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Voce informou {} numeros pares e a soma foi {}'.format(cont,soma))

