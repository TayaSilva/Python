print("====== LOJA DA TAYA ======")
preço = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO \n"
      "[ 1 ] á vista (Pix ou dinheiro) \n"
      "[ 2 ] á vista no cartão \n"
      "[ 3 ] 2x no cartão de credito \n"
      "[ 4 ] 3x ou mais no cartão \n")

dig = int(input("Digite a opção desejada: "))

if dig == 1:
    total = preço - (preço * 10/100)
    print("O valor a ser pago é {:.2f} com 10% de desconto".format(total))

elif dig ==2:
    total = preço - (preço * 5/100)
    print("O valor a ser pago é {:.2f} com 5% de desconto".format(total))

elif dig == 3:
    total = preço /2
    print("O valor a ser pago é {:.2f} em 2x no cartão de {:.2f} ".format(preço, total))

elif dig == 4:
    total = preço + (preço * 20/100)
    print("O valor a ser pago é {:.2f} com acrescimo de 20% no valor ".format(total))
else:
    print("Opção invalida!")



