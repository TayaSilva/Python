'''Fatiamento de string, o ultimo valor não entra, exemp frase[9:13] vai do 9 ao 12'''

frase = 'Taiane Nascimento da silva'
print(frase[3:10:2])

print(frase.count('a'))
'''Ver quantos 'A' tem na frase'''

print(frase.find('ai'))
'''se a frase dentro de find não existir ele retorna -1'''

print('Taiane'in frase)
'''Fala se tem Taiane na frase sim ou não'''

print(frase.replace('Taiane','Julia'))
'''Substitui uma string'''

print(frase.upper())
'''Deixa tudo em maiusculo'''

print(frase.lower())
'''Deixa tudo em minusculo'''

print(frase.capitalize())
'''Deixa só a primeira letra da frase em maiusculo'''



print(frase.title())
'''Deixa todas as primeiras letras de cada palavra em maiusculo'''

print(frase.strip())
'''Remove espaços desnecessarios'''



