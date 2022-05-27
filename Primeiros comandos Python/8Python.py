medida = float(input("Digite uma distancia em metros "))
cm = medida*100
mm = medida*1000
km = medida/1000
print('a medida de {}m corresponde a {:.2f}cm e {:.2f}mm'.format(medida,cm,mm))
print('e {}m em Km é {}'.format(medida,km))