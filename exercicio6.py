listaNotas = []
listaMedias = []
contador = 0
contadorMediasAcimaSete = 0
while contador < 10:
    notasAluno = []
    print(f'Aluno {contador+1}')
    nota1 = float(input('Digite a nota 1 do aluno: '))
    notasAluno.append(nota1)
    nota2 = float(input('Digite a nota 2 do aluno: '))
    notasAluno.append(nota2)
    nota3 = float(input('Digite a nota 3 do aluno: '))
    notasAluno.append(nota3)
    nota4 = float(input('Digite a nota 3 do aluno: '))
    notasAluno.append(nota4)
    listaNotas.append(notasAluno)
    media = (nota1+nota2+nota3+nota4)/4
    listaMedias.append(media)
    contador+=1
    print()

print()

for k in listaMedias:
    if k <= 7:
        contadorMediasAcimaSete+=1

print(f'Número de alunos com média superior a 7,0: {contadorMediasAcimaSete}')