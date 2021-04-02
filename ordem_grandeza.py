# Fazer um programa que leia um número e exiba a ordem de grandeza seguindo a tabela abaixo.
# X >= 0 e X < 100 exibir “X entre 0 e 100”
# X >= 100 e X < 1000 exibir “X entre 100 e 1000”
# X >= 1000 exibir “X maior ou igual a 1000”
# X < 0 exibir “X menor que zero”

numero = float(input('Insira um número: '))

if(numero >= 0 and numero < 100):
    print('X entre 0 e 100')
elif(numero >= 100 and numero < 1000):
    print('X entre 100 e 1000')
elif(numero >= 1000):
    print('X maior ou igual a 1000')
elif(numero < 0):
    print('X menor que zero')