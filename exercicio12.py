contador = 1
listaIdades = []
listaAlturas = []
somaAlturas = 0
contadorAlunosAcimaTrezeAnosAcimaMediaAltura = 0

print(f'LISTA DE CADASTRO DE IDADES E ALTURAS DOS ALUNOS')
while contador < 31:
    print(f'Aluno {contador}')
    idade = int(input('Digite a idade: '))
    listaIdades.append(idade)
    altura = float(input('Digite a altura: '))
    somaAlturas = somaAlturas+altura
    listaAlturas.append(altura)
    contador+=1

mediaAltura = somaAlturas/30

for k in range(0,30):
    if listaIdades[k] > 13 and listaAlturas [k] > mediaAltura:
        contadorAlunosAcimaTrezeAnosAcimaMediaAltura+=1
    else:
        continue

print()
print()
print(f'Número de alunos acima de treze anos e acima da média de altura: {contadorAlunosAcimaTrezeAnosAcimaMediaAltura}')