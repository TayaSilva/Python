opç = ''
tprç = maism = menor = cont = bar = 0
while True:

    print("-="*5, "LOJAS TAYA", "-="*5)
    prod = str(input("Nome do produto: ")).upper().strip()
    prç = float(input("Preço: R$"))
    cont+=1
    tprç += prç

    if prç > 1000:
        maism += 1


    if cont ==1 or prç < menor:
        menor = prç
        bar = prod


    opç = str(input("Deseja continuar comprando: [S/N]")).upper()[0].strip()
    while opç not in 'SN':
        print("Opção invalida")


    if opç == 'N':
        print("-="*5,"SESSÃO DE COMPRAS ENCERRADA! VOLTE SEMPRE", "-="*5)
        break
print("Você gastou R${:.2f}".format(tprç))
print(f"{maism} custaram mais de R$1000,00")
print("O proturo mais barato chama {} e custa R${:.2f}".format(bar,menor))