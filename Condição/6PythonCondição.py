n = int(input("Me fale um numero qualquer e eu direi se é PAR ou IMPAR: "))
res = n % 2
if res == 1:
    print("\033[1;35mO numero {} é Impar!!!".format(n))
else:
    print("\033[1;36mO numero {} é Par!!!".format(n))