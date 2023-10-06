listaCaracteres = []
contador = 0
contaConsoantes = 0
consoantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                    "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "ç"
                    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                    "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
while contador < 10:
    if contador == 0:
        caractere = input('Digite um caractere: ')
    else:
        caractere = input('Digite outro caractere: ')
    if len(caractere) >= 2 or caractere.isdigit():
        print('Digito inválido! Tente novamente')
    else:
        contador+=1
        listaCaracteres.append(caractere)

for k in listaCaracteres:
    for l in consoantes:
        if k == l:
            contaConsoantes += 1
        else:
            contaConsoantes += 0
print()
print('Lista de caracteres:')
print(listaCaracteres)
print()
print(f'Número de consoantes: {contaConsoantes}')