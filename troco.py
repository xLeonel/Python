# a. Escreva um programa que leia um valor e que imprima a quantidade de cédulas
# necessárias para pagar esse mesmo valor. Para simplificar utilize números inteiros e com
# cédulas de R$50, R$20, R$10, R$4 e R$1. Após concluído, faça testes com os seguintes
# valores: 50, 745, 384, 2, 7 e 1.

# b. Modifique o item a para trabalhar com nota de R$ 100,00. O que acontece se for digitado
# 0 (zero) no valor a pagar? Ajuste seu programa.

# c. Modifique o programa do item a para aceitar valores decimais, ou seja, também contar
# moedas de R$0.01, R$0.02, R$0.05, R$0.10, e R$0.50.
# d. No item d, o que acontece se digitarmos 0.001? Caso ele não funcione, altere-o de forma
# a corrigir esse problema.

# e. Reescreva de forma a continuar executando até que o valor digitado seja 0. Utilize
# repetições aninhadas.


import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def contas_cedulas(numb):
    cem = int(numb / 100)
    numb = numb - (cem*100)

    cinquenta = int(numb/50)
    numb = numb - (cinquenta*50)

    vinte = int(numb/20)
    numb = numb - (vinte*20)

    dez = int(numb/10)
    numb = numb - (dez*10)

    quatro = int(numb/4)
    numb = numb - (quatro*4)

    um = int(numb/1)
    numb = numb - (um*1)

    cinquentaCents = int(numb/0.50)
    numb = numb - (cinquentaCents*0.50)

    dezCents = int(numb/0.10)
    numb = numb - (dezCents*0.10)

    cincoCents = int(numb/0.05)
    numb = numb - (cincoCents*0.05)

    doisCents = int(numb/0.02)
    numb = numb - (doisCents*0.02)

    umCents = int(numb/0.01)
    numb = numb - (umCents*0.01)

    validarNumero = (cem*100) + (cinquenta*50) + (vinte*20) + (dez*10) + (quatro*4) + (um*1) + (
        cinquentaCents*0.5) + (dezCents*0.1) + (cincoCents*0.05) + (doisCents*0.02) + (umCents*0.01)

    if(cem != 0):
        print('Notas R$100,00 = ', cem)
    if(cinquenta != 0):
        print('Notas R$ 50,00 = ', cinquenta)
    if(vinte != 0):
        print('Notas R$ 20,00 = ', vinte)
    if(dez != 0):
        print('Notas R$ 10,00 = ', dez)
    if(quatro != 0):
        print('Notas R$  4,00 = ', quatro)
    if(um != 0):
        print('Notas R$  1,00 = ', um)
    if(cinquentaCents != 0):
        print('Moedas R$ 0,50 = ', cinquentaCents)
    if(dezCents != 0):
        print('Moedas R$ 0,10 = ', dezCents)
    if(cincoCents != 0):
        print('Moedas R$ 0,05 = ', cincoCents)
    if(doisCents != 0):
        print('Moedas R$ 0,02 = ', doisCents)
    if(umCents != 0):
        print('Moedas R$ 0,01 = ', umCents)
    if (validarNumero != numeroReal):
        print('Moedas R$ 0,01 = ', 1)

print('Para interromper o saque insira o numero 0 (zero)')
print('')
numero = float(input('Valor para sacar: '))
numeroReal = numero

while(numero != 0):
    while(numeroReal < 0.01):
        print('Você não pode sacar {} reais. Digite outro valor diferente de {}.'.format(
            numero, numero))
        numero = float(input('Valor para sacar: '))
        numeroReal = numero

    contas_cedulas(numero)
    input('Valor sacado com Sucesso. Pressione "Enter" para realizar outro saque.')
    clear()
    print('Para interromper o saque insira o numero 0 (zero)')
    print('')
    numero = float(input('Valor para sacar: '))
    numeroReal = numero
