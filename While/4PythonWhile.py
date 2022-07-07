n = int(input("Digite um numero para calcular o fatorial: "))
c = n
f = 1
while c>0:
    print("{} ".format(c), end='')
    print("X " if c >1 else " = " , end="")
    f *= c
    c -=1
print("{}".format(f))

