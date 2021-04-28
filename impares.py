# Escreva um programa que mostre os números de 1 até um numero digitado pelo usuário, mas,
# apenas os números impares.

numero = int(input('Digite um numero: '))

for x in range(numero):
  if (x % 2) != 0:
    print(x, end=" ")