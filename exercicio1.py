listaNumeros = []

for k in range(0, 5):
    if k == 0:
        numero = int(input('Digite um numero inteiro: '))
    else:
        numero = int(input('Digite outro numero inteiro: '))
    listaNumeros.append(numero)

print(listaNumeros)