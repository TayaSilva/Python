media = soma = quant = maior = menor =0
opç = 'S'

while opç in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    quant +=1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    opç = str(input("Quer continuar {S/N}")).upper().strip()[0]
media = soma / quant
print("Você digitou {} numeros e a média dos numeros foi {:.2f}".format(quant,media))
print("O maior valor foi {} e o menor {}".format(maior, menor))
