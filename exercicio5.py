listaNumeros = []
listaPares = []
listaImpares = []
contador = 0

while contador < 20:
    if contador == 0:
        numero = input('Digite um número: ')
    else:
        numero = input('Digite outro número: ')
    if not numero.isdigit():
        print('Erro! Você deve digitar um número inteiro!')
        continue
    else:
        numero = int(numero)
        listaNumeros.append(numero)
        if numero%2==0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)
        contador+=1
print()
print()
print(f'Lista de números: {listaNumeros}')
print(f'Lista de números pares: {listaPares}')
print(f'Lista de números ímpares: {listaImpares}')