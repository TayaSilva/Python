print("-="*5, "10 TERMOS DE UMA PA", "-="*10)

prim = int(input("Digite o  termo: "))
raz = int(input("Digite a razão: "))
print("-="*26)


termo = prim
cont = 1

while cont <=10:
    print("{} - ".format(termo), end="")
    termo += raz
    cont += 1
