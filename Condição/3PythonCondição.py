n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
m = (n1 + n2 + n3 + n4)/4
if m >= 6.0:
    print("Sua nota foi boa, PARABENS!!, nota {:.1f}".format(m))
if m == 5:
    print("Seu nota foi mediana, nota {:.1f}".format(m))
else:
    print("Sua nota foi ruim, nota {:.1f}".format(m))

