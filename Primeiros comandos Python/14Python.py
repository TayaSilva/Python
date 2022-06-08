km = float(input("Informe a quantidade de KM rodados: "))
d = int(input("Informe a quantide de dias que o carro foi alugado: "))

dias = d * 60
k = km * 0.15

print("O total a pagar é R${}".format(dias + k))