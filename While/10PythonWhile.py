num = soma = cont = 0

while True:
    num = int(input("Digite um numero [PARA ENCERRAR DIGITE 999]:   "))
    cont += 1
    if num == 999:
        break

    soma += num
print(f"A soma dos valores é {soma},e foram feitas {cont} tentativas")