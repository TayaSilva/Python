print("-="*5, "TABUADA", "-="*5)

n = int(input("Digite o numero da tabuada que deseja: "))

print("-="*15)

for x in range (0,11):
    print('{} X {} = {}'.format(n,x,n*x))
