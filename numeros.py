# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números
# até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números
# digitados, assim como a soma e a média aritmética. 

numero = int(input('Digite um numero: '))
numeros = []
total = 0

while(numero != 0):
    numeros.append(numero)
    numero = int(input('Digite outro numero: '))

if(numero == 0):
    for x in numeros:
        total += x
    print('Soma dos numeros: ', total)
    print('Média aritmética: ', total / len(numeros))



      