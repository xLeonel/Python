# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
# resultado da operação solicitada.

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
operacao = input('qual operacao matematica basica voce quer fazer (+ - * /): ')

operacoes = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}

resultado = operacoes.get(operacao, 'operacao nao encontrada')

print('Resultado: ', resultado)

