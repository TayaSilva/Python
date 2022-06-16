from random import randint
from time import sleep #dar um tempo pra retorno da resposta

pc = randint(0,5)
print("Adivinhe no numero que eu pensei entre 0 a 5 ... adivinhe")

jg = int(input("O numero que eu pensei foi: "))
print("PROCESSANDO JOGO ...")
sleep(2)

if jg == pc:
    print("PARABÉNS, VOCÊ É UM GENIO!!! EU PENSEI EXATAMENTE NO NUMERO {}".format(pc))
else:
    print("Você perdeu, eu pensei no numero {} e não no {}".format(pc,jg))


