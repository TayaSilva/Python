num = int(input("Digite um numero: "))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end=" ")
        tot += 1
    else:
        print('\033[1;36m', end=" ")
    print('{}'.format(c), end=" ")
print('\nO numero {} foi divisivel {} vezes'.format(num, tot))