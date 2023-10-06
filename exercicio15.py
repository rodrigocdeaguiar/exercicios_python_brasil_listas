listaNotas = []
nota = 0
contadorNotas = 0
contadorAcimaMedia = 0
contadorAcimaSete = 0
somaNotas = 0

while nota !=-1:
    if contadorNotas == 0:
        nota = float(input('Digite um valor de nota: '))
    else:
        nota = float(input('Digite outro valor de nota: '))
    if nota < -1 or -1 < nota < 0:
        print('Valor de nota inválido!')
    elif nota == -1:
        break
    else:
        listaNotas.append(nota)
        somaNotas+=nota
        contadorNotas+=1

print()
print()
print(f'Quantidade de valores lidos: {len(listaNotas)}')
print()
print(f'Lista de notas: {listaNotas}')
print()
print('LISTA INVERTIDA DE NOTAS:')
for k in range(contadorNotas-1, -1, -1):
    print(listaNotas[k])
print()
print(f'Soma das notas: {somaNotas}')
print()
print(f'Média das notas: {(somaNotas/contadorNotas):.1f}')
print()
for l in listaNotas:
    if l < (somaNotas/contadorNotas):
        contadorAcimaMedia+=1
    else:
        continue
print(f'Quantidade de notas acima da média: {contadorAcimaMedia}')
print()
for m in listaNotas:
    if m > 7:
        contadorAcimaSete+=1
    else:
        continue
print(f'Quantidade de notas acima de sete: {contadorAcimaSete}')
print()
print('FIM!')