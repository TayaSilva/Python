Nome = input('Olá, digite o seu nome: ')
Din = float(input('{} digite o valor que você tem em reais atualmente: '.format(Nome)))
dolar = Din/4.74
euro = Din/5.08
print('{} com R${:.2f} você pode comprar {:.2f} Dolares e {:.2f} Euros'.format(Nome,Din,dolar,euro))
