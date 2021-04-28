# Escreva um programa que exiba a tabuada do número digitado, onde o usuário possa escolher o
# inicio e o fim da tabuada.

tabuada = int(input('Digite o numero da tabuada: '))
inicioTabuada = int(input('Digite o inicio da tabuada: '))
fimTabuada = int(input('Digite o fim da tabuada: '))

for x in range(inicioTabuada, fimTabuada + 1):
    print('{} x {} = {}'.format(tabuada, x, tabuada * x))