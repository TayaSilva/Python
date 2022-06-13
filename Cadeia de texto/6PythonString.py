frase = str(input("Digite uma frase: ")).strip().upper()


print("A letra A apareceu {} vezes".format(frase.count('A')))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
#esse mais 1 é pq no progrma começa com 0
print("A ultima letra A apareceu na posição {}".format(frase.rfind("A")+1))
