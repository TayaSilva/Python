km = float(input("Digite a velocidade do carro: "))
new = (km - 80) *7
if km >80:
   print("Você ultrapassou a velocidade indicada e foi multado no valor de \033[1;31mR${:.2f}".format(new))
   print("\033[1;31mTenha um bom dia e PRESTE MAIS ATENÇÃO NO TRÂNSITO!!!")
else:
    print("\033[1;34mVocê está dentro da velocidade correta, PARABÉNS")
    print("\033[1;34mTenha um bom dia e dirija com segurança!!!")

