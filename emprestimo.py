# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O
# programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da
# prestação como sendo o valor da casa a comprar dividido pelo numero de meses a pagar.

valorCasa = float(input('Insira o valor da casa: '))

salario = float(input('Insira o seu salário: '))

anos = int(input('Em quantos anos irá pagar: '))

parcela = valorCasa / anos

if(parcela > (salario * 0.3)):
    print('Voce não pode comprar essa casa, salário insuficiente')
else:
    print('O valor da parcela R$: ', parcela)
