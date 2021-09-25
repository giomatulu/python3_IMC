# CALCULADORA DE IMC

nome = input('Olá! Qual o seu nome?')
altura = float(input(f'{nome.capitalize()}, '
'por favor digite sua altura em metros:'))
peso = float(input('Digite o seu peso em Kg:'))

calculo_imc = (peso / (altura * altura))
imc = '%.1f' % calculo_imc
print(f'\nSeu imc é: {imc}')

# abaixo confere se o peso está ideal

if (float(imc) < 18.5):
    print('Você está abaixo do peso ideal.')
if (float(imc) > 18.5 and float(imc) < 24.9):
    print('Peso ideal, parabéns!')
if (float(imc) > 25.0 and float(imc) < 29.9):
    print('Levemente acima do peso.')
if (float(imc) > 30.0 and float(imc) < 34.9):
    print('Obesidade grau I, cuidado!')
if (float(imc) > 35.0 and float(imc) < 39.9):
    print('Obesidade grau II, isso é severo!')
if (float(imc) > 40.0 ):
    print('Obesidade grau III, isso é mórbido!')



