from math import hypot
'''op = float(input("Digite o valor do cateto oposto"))
adj = float(input("Digite o valor do cateto adjacente"))

hi = (op **2 + adj) ** (1/2)

print("A hipotenusa vai medir {:.2f}".format(hi))'''

op = float(input("Digite o valor do cateto oposto"))
adj = float(input("Digite o valor do cateto adjacente"))
hi = hypot(adj, op)

print("A hipotenusa vai medir {:.2f}".format(hi))