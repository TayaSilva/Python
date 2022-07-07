from random import randint
from time import sleep

computador = randint(0,10)
palpt = 0
acertou = False


print("Olá, sou o Pici, o seu computador \nEu pensei  em um numero entre 0 e 10, duvido você acertar")

while not acertou:
    esc = int(input("Escolha um numero: "))
    palpt +=1




    if esc == computador:
        acertou = True
    else:
        if esc <computador:
            print("O computador escolhe o numero ...")
            sleep(1)
            print("{}".format(computador))
            print("Foi por pouco, tinha pensado em um numero maior que {}\n Vou jogar novamente, tente de novo".format(esc))
        elif esc > computador:
            print("O computador escolhe o numero ...")
            sleep(1)
            print("{}".format(computador))
            print("Por pouco ... escolhi um numero menor que o seu {}\n Vou jogar novamente, tente de novo".format(esc))




print("\033[1;32mParabéns, nós pensamos igual!!")
print("Você acertou com {} tentativas".format(palpt))