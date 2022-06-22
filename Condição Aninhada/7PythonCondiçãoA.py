print("Programa de calculo de IMC")
print("--------------------------------------------------")

peso = float(input("Digite seu peso (Kg): "))
alt = float(input("Digite sua altura (m): "))

imc = peso / (alt **2)

print("O IMC dessa pessoa é de {:.1f}".format(imc))

if imc <= 18.5:
    print("Voce está abaixo do peso")
elif imc >=18.5 and imc <=25:
    print("Você está no seu peso ideal")
elif imc >=25 and imc <=30:
    print("Você está com sobrepeso, atenção!!!")
elif imc >=30 and imc <=40:
    print("Você está obeso!!! Cuidado")
else:
    print("Você está com obesidade morbita, procure ajuda!")


