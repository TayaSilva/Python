print("Programa de calculo de emprestimo, responda as questões a seguir!!")

print("--------------------------------")

casa = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual o seu salario atual? R$"))
anos = int(input("Em quantos anos deseja pagar? R$"))

pres = casa / (anos * 12) #valor da casa dividido pelos meses que ele quer pagar
min = sal * 30 / 100 # PRa descobrir o valor dos 30% do salario

print("Para pagar uma casa de R${:.2f} em {} anos o valor sera de R${:.2f}".format(casa,anos,pres))

if pres < min:
    print("\033[1;35mEmprestimo aprovado!!!")
elif pres == min:
    print("Valor sob consulta")
else:
    print("\033[1;31mValor NEGADO!!!")











