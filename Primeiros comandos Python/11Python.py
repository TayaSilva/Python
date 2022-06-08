preço = float(input('Qual o preço do produto R$: '))
novo = preço - (preço * 5 / 100)
print("O produto que estava R${:.2f} fora da promoção, se encontra no valor de R${:.2f} com o desconto de 5%".format(preço, novo))