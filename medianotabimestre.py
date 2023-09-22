# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

nota1 = float(input('Qual sua nota do 1 bimestre?\n'))
nota2 = float(input('Qual sua nota do 2 bimestre?\n'))
nota3 = float(input('Qual sua nota do 3 bimestre?\n'))
nota4 = float(input('Qual sua nota do 4 bimestre?\n'))

medianota = (nota1+nota2+nota3+nota4)/4

print(f'Sua média desse ano foi {medianota}!\n')

if medianota <= 7:
    print('Aprovado')
if medianota == 10:
    print('Aprovado com 10 em todos os semestres!')
else:
    print('Reprovado')
