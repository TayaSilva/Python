
idade18 = masc = idadeF= 0
while True:
    prox = 'NnSs'
    sexo = ' '

    (print("*"*10, "SENSO 2022","*"*10))
    nome = str(input("Digite o seu nome: ")).upper()[0].strip()
    idade =  int(input("Digite a sua idade: "))
    while sexo not in 'MF':
        sexo = str(input("Digite o seu sexo [M/F]: ")).upper()[0].strip()
    if idade >=18:
        idade18 += 1
    if sexo == "M":
        masc+= 1
    if sexo == "F" and idade <=20:
        idadeF += 1

    while prox not in 'SN':
        prox = str(input("Quer continuar? [S/N]: ")).upper()[0].strip()

    if prox in "Nn":
        print(f"Tivemos {idadeF} mulheres com menos de 20 anos ")
        print(f"{idade18} pessoas com mais de 18 anos e")
        print(f"{masc} homens cadastrados")
        breaks

print("\033[1;34mPrograma encerrado!")