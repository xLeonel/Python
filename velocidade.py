# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80
# km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da
# multa, cobrando R$ 5,00 por km acima de 80 km/h.

velocidade = int(input('velocidade do carro: '))

if(velocidade > 80):
    multa = (velocidade - 80) * 5
    print('Voce foi multado em R$: ', multa)
else:
    print('Voce esta dentro do limite de velocidade.')