vetorUm = []
vetorDois = []
vetorTres = []
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

for k in range(0,10):
    vetorTres.append(vetorUm[k])
    vetorTres.append(vetorDois[k])

print(f'Vetor 1: {vetorUm}')
print(f'Vetor 2: {vetorDois}')
print(f'Vetor 3: {vetorTres}')