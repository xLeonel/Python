# Faça um programa solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor
# do desconto e o preço a pagar.

preco = int(input('Preço inicial: '))
desconto = float(input('Desconto em %: '))

desconto = (preco * desconto) / 100
precoFinal = preco - desconto

print('O valor do seu desconto será de {}. O valor final com desconto será de {}.'.format(desconto, precoFinal))


