# Escreva um programa que verifique se um numero é palíndromo. Um número palíndromo se
# continua o mesmo caso seus dígitos sejam invertidos. Exemplo: 454, 10501. 

numero = input('Insira um numero: ')

numeroInvertido = numero[::-1]

if(numero == numeroInvertido):
    print('O número {} é um palíndromo'.format(numero))
else :
    print('O número {} não é um palíndromo'.format(numero))
    

