from datetime import date

print("Programa de classificação de atletas em suas categorias")
print("--------------------------------------------------------")

ano = int(input("Digite seu ano de nascimento: "))
data = date.today().year
idade = data - ano

if data - ano <= 9:
    print("Você tem {} anos e pertence a categoria MIRIM".format(idade))
elif data - ano <=14:
    print("Você tem {} anos e pertence a categoria INFANTIL".format(idade))
elif data - ano <=19:
    print("Você tem {} anos pertence a categoria JUNIOR".format(idade))
elif data - ano <=25:
    print("Você tem {} anos e pertence a categoria SENIOR".format(idade))
else:
    print("Você tem {} anos e esta na categoria MASTER".format(idade))

