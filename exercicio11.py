vetorUm = []
vetorDois = []
vetorTres = []
vetorQuatro = []
contador = 0

print('Insira os números do primeiro vetor: ')
while contador < 10:
    if contador == 0:
        numero = int(input('Digite um número inteiro: '))
    else:
        numero = int(input('Digite outro número inteiro: '))
    vetorUm.append(numero)
    contador+=1

print()
print('Insira os números do segundo vetor: ')
contador = 0
while contador < 10:
    if contador == 0:
        numero = int(input('Digite um número inteiro: '))
    else:
        numero = int(input('Digite outro número inteiro: '))
    vetorDois.append(numero)
    contador+=1

print()
print('Insira os números do terceiro vetor: ')
contador = 0
while contador < 10:
    if contador == 0:
        numero = int(input('Digite um número inteiro: '))
    else:
        numero = int(input('Digite outro número inteiro: '))
    vetorTres.append(numero)
    contador+=1


for k in range(0,10):
    vetorQuatro.append(vetorUm[k])
    vetorQuatro.append(vetorDois[k])
    vetorQuatro.append(vetorTres[k])


print(f'Vetor 1: {vetorUm}')
print(f'Vetor 2: {vetorDois}')
print(f'Vetor 3: {vetorTres}')
print(f'Vetor 4: {vetorQuatro}')