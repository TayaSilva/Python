print("-="*5, "10 TERMOS DE UMA PA", "-="*10)

prim = int(input("Digite o  termo: "))
raz = int(input("Digite a razão: "))
decimo = prim + (10 -1) * raz
print("-="*26)


for prim in range (prim,decimo + raz ,raz):
    print('{}'.format(prim), end = ' - ')
