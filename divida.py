# Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte
# também o valor mensal que será pago. Imprima o número de meses para que a divida seja
# paga, o total pago e o total de juros pago.

divida = float(input('valor da divida: '))
jurosMensal = float(input('valor dos juros mensal: '))
valorMes = float(input('quanto sera pago por mes: '))

valorTotal = divida + (divida * jurosMensal)
juros = valorTotal - divida
numMes = valorTotal / valorMes

print('')
print('número de meses para que a divida seja paga: ', numMes)
print('total pago: ', valorTotal)
print('total de juros pago: ', juros)