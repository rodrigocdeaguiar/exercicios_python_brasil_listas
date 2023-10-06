listaNotas = []

for k in range(0,4):
    if k == 0:
        nota = float(input('Digite uma nota: '))
    else:
        nota = float(input('Digite outra nota: '))
    listaNotas.append(nota)

print()
print(f'Nota 1: {listaNotas[0]}')
print(f'Nota 2: {listaNotas[1]}')
print(f'Nota 3: {listaNotas[2]}')
print(f'Nota 4: {listaNotas[3]}')
print()
media = (listaNotas[0] + listaNotas[1] + listaNotas[2] + listaNotas[3])/4
print(f'Média: {media:.1f}')