print("-="*5, "10 TERMOS DE UMA PA", "-="*10)

prim = int(input("Digite o  termo: "))
raz = int(input("Digite a razão: "))
print("-="*26)

total =0
termo = prim
cont = 1
mais = 10

while mais !=0:
    total = total + mais
    while cont <= total:
        print("{} - ".format(termo), end="")
        termo += raz
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer mostrar? "))

print("Programa Finalizado")
