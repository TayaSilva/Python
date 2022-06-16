km = float(input("Qual a distancia em KM é a sua viagem: "))
print("Você está prestes a começar uma viagem de {:.2f} KM".format(km))

if km <= 200:
    preço = km * 0.50
    print("O valor cobrado é R${:.2f}".format(preço))
else:
    preço = km * 0.45
    print("O valor cobrado é R${:.2f}".format(preço))