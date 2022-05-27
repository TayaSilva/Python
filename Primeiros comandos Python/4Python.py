nome = input('Olá jovem, como eu devo te chamar? ')
print('Fechou {}, vamos fazer umas contas agora'.format(nome))
n1 = int(input('Digite um numero'))
n2 = int(input('Bacana!!!, agora digite outro numero {} '.format(nome)))
soma = n1+n2
mult = n1*n2
div = n1/n2
pot = n1**n2
sub = n1-n2

print('A soma dos numeros que você digitou é {},'
      '\n a subtração é {}, '
      '\n a multiplicação é {}, '
      '\n a divisão é {:.3f},' # vai aparecer apenas 3 casas na divisão
      '\n e a potencia desses dois é {}'.format(soma,sub,mult,div,pot))

print('Obrigado por participar {}, beijinhos e até a proxima!!'.format(nome))

