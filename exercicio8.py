contadorProgressivo = 1
contadorRegressivo = 5
listaIdades = []
listaAlturas = []
while contadorProgressivo < 6:
    print(f'Pessoa {contadorProgressivo}')
    idade = int(input('Digite a idade: '))
    listaIdades.append(idade)
    altura = float(input('Digite a altura: '))
    listaAlturas.append(altura)
    contadorProgressivo+=1

print()
print()

for k in range(4,-1,-1):
    print(f'Pessoa {contadorRegressivo}:\n'
          f'Idade: {listaIdades[k]} ano(s)\n'
          f'Altura: {listaAlturas[k]} m')
    print()
    contadorRegressivo-=1