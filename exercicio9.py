lista = []
listaQuadrados = []
contador = 0
somaQuadrados = 0

while contador < 10:
    if contador == 0:
        numero = int(input('Digite um número inteiro: '))
        lista.append(numero)
    else:
        numero = int(input('Digite outro número inteiro: '))
        lista.append(numero)
    contador+=1

for k in lista:
    quadrado = k**2
    listaQuadrados.append(quadrado)
    somaQuadrados = somaQuadrados + quadrado

print()
print(f'Lista: {lista}')
print(f'Lista dos quadrados: {listaQuadrados}')
print(f'Soma dos quadrados dos elementos da lista: {somaQuadrados}')