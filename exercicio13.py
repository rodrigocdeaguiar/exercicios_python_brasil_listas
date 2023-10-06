mesesAno = ['1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho',
            '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']
mediasTemperatura = []
somaTemperaturas = 0

for k in range(0,12):
    print(f'Mês {mesesAno[k]}')
    media = float(input('Registre a média de temperatura do mês, em °C: '))
    mediasTemperatura.append(media)
    somaTemperaturas = somaTemperaturas+media

mediaAnual = somaTemperaturas/12
print()
print(f'Média anual de temperatura: {mediaAnual:.1f}°C')
print()
print('MESES DE TEMPERATURAS ACIMA DA MÉDIA ANUAL: ')
for i in range (0,12):
    if mediasTemperatura[i] > mediaAnual:
        print(f'Més: {mesesAno[i]}\n'
              f'Temperatura: {mediasTemperatura[i]}°C')