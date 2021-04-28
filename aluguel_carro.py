# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a
# pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = int(input('Km percorridos: '))
dias = int(input('Dias pelos quais o carro foi alugado: '))

preco = ((km * 0.15) + (dias * 60))

print('Preco a ser pago: ', preco)