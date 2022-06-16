from datetime import date
ano  = int(input("Que ano você quer analisar? Ou digite 0 para o ano atual: "))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[1;32mO ano {} é BISSEXTO!!!".format(ano))
else:
    print("\033[1;32mO ano {} NÃO é Bissexto".format(ano))