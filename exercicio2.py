listaNumeros = []
listaNumerosInversa = []

for k in range(0, 10):
    if k == 0:
        numero = int(input('Digite um numero inteiro: '))
    else:
        numero = int(input('Digite outro numero inteiro: '))
    listaNumeros.append(numero)

print(listaNumeros)

for i in range(-1,-11,-1):
    listaNumerosInversa.append(listaNumeros[i])

print(listaNumerosInversa)