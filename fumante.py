# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ela já fumou. Considere que um
# fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida um fumante
# perderá. Exiba o total em dias.

cigarroDia = int(input('Quantos cigarros voce fuma por dia? '))
anos = int(input('Quantos anos voce fuma? '))

tempoRestante = ((cigarroDia * 10) * (365.25 * anos)) / 1440

print('Voce tem {} dias a menos de vida'.format(tempoRestante))
