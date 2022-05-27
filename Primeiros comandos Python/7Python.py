Nome = input('Seja bem vindo ao sistema de calculo de notas, digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
n3 = float(input('Digite a terceira nota '))
m = (n1+n2+n3)/3
print('A média do(a) aluno(a) {} é igual a soma do {} + {} + {} divido por 3, tendo o resultado de {:.3}'.format(Nome,n1,n2,n3,m))