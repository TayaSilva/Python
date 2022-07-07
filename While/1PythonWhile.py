
sexo = str(input("Digite o seu sexo M/F: ")).upper()[0].strip()
while sexo not in 'M''F':
    sexo = str(input("Sexo incorreto, por favor digite o seu sexo M/F: ")).upper()[0].strip()
print("sexo {} registrado com sucesso".format(sexo))
