# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial, I para
# industrial e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir:
# • Residencial: Até 500 kWh – R$ 0,40 e acima de 500 kWh – R$ 0,65.
# • Comercial: Até 1000 kWh – R$ 0,55 e acima de 1000 kWh – R$ 0,60.
# • Industrial: Até 5000 kWh – R$ 0,55 e acima de 5000 kWh – R$ 0,60

def calculo_residencial(kwh):
    if(kwh <= 500):
        return kwh * 0.4
    else:
        return kwh * 0.65

def calculo_comercial(kwh):
    if(kwh <= 1000):
        return kwh * 0.55
    else:
        return kwh * 0.60       

def calculo_industrial(kwh):
    if(kwh <= 5000):
        return kwh * 0.55
    else:
        return kwh * 0.60

kwh = int(input('a quantidade de kWh consumida: '))
instalacao = input('tipo de instalação: R para residencial, I para industrial e C para comércios: ')

operacoes = {'r': calculo_residencial(kwh), 'i': calculo_industrial(kwh), 'c': calculo_comercial(kwh)}

valor = operacoes.get(instalacao.lower(), 'valor nao encontrado')

print('Valor a pagar pelo fornecimento de energia elétrica, R$: ', valor)