print("Programa de calculo de notas!")
print('--------------------------------------------------')

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2 )/2

if media < 5:
    print("\033[1;31mVocê tirou nota {:.2f}, e está em RECUPERAÇÃO!!!".format(media))
elif media > 6:
    print("\033[1;32mVocê tirou nota {:.2f} e esta APROVADO!!!".format(media))
elif media ==5 or 6:
    print("\033[1;36mVocê tirou nota {:.2f}, está na média, porém pode se esforçar mais!".format(media))