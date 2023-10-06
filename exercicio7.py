listaNumeros = []
acumulador = 0
for k in range(0,5):
    if k == 0:
        numero = int(input('Digite um número: '))
        listaNumeros.append(numero)
    else:
        numero = int(input('Digite outro número: '))
        listaNumeros.append(numero)

for i in listaNumeros:
    if acumulador == 0:
        multiplicacao = listaNumeros[0] * listaNumeros[1]
        soma = listaNumeros[0] + listaNumeros[1]
        acumulador+=1
    elif acumulador == 1:
        acumulador += 1
        continue
    else:
        multiplicacao = multiplicacao * i
        soma = soma + i
        acumulador+=1


print()
print(f'Lista de números: {listaNumeros}')
print(f'Resultado da multiplicação: {multiplicacao}')
print(f'Resultado da soma: {soma}')