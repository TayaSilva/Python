sal = float(input("Digite o valor do seu salario: "))

if sal <= 1250:
    novo = sal + (sal * 15 /100)
    print("Seu salario atual, com um aumento de 15% é de \033[1;32mR${:.2f}".format(novo))
else:
    novo = sal + (sal * 10/100)
    print("Seu salario atual, com um aumento de 10% é de \033[1;32mR${:.2f}".format(novo))