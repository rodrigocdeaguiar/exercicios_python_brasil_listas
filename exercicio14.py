contador = 0
listaRespostas = []
telefonouVitima = 'chao'
esteveLocalCrime = 'chao'
moraPertoVitima = 'chao'
deviaParaVitima = 'chao'
trabalhouComAVitima = 'chao'

while telefonouVitima.lower() != 'sim' or telefonouVitima.lower() != 'não':
    telefonouVitima = input('Telefonou para a vítima? ')
    if telefonouVitima.lower() == 'sim' or telefonouVitima.lower() == 'não':
        listaRespostas.append(telefonouVitima)
        break
    else:
        continue
while esteveLocalCrime.lower()!='sim' or esteveLocalCrime.lower()!='não':
    esteveLocalCrime = input('Esteve no local do crime? ')
    if esteveLocalCrime.lower() == 'sim' or esteveLocalCrime.lower() == 'não':
        listaRespostas.append(esteveLocalCrime)
        break
    else:
        continue
while moraPertoVitima.lower()!='sim' or moraPertoVitima.lower()!='não':
    moraPertoVitima = input('Mora perto da vítima? ')
    if moraPertoVitima.lower() == 'sim' or moraPertoVitima.lower() == 'não':
        listaRespostas.append(moraPertoVitima)
        break
    else:
        continue
while deviaParaVitima.lower()!='sim' or deviaParaVitima.lower()!='não':
    deviaParaVitima = input('Devia para a vítima? ')
    if deviaParaVitima.lower() == 'sim' or deviaParaVitima.lower() == 'não':
        listaRespostas.append(deviaParaVitima)
        break
    else:
        continue
while trabalhouComAVitima.lower()!='sim' or trabalhouComAVitima.lower()!='não':
    trabalhouComAVitima = input('Devia para a vítima? ')
    if trabalhouComAVitima.lower() == 'sim' or trabalhouComAVitima.lower() == 'não':
        listaRespostas.append(trabalhouComAVitima)
        break
    else:
        continue

for resposta in listaRespostas:
    if resposta == 'sim':
        contador+=1
    else:
        continue

print()
print()

if contador == 2:
    print('Suspeita')
elif contador == 3 or contador == 4:
    print('Cúmplice')
elif contador == 5:
    print('Assassino')
else:
    print('Inocente')