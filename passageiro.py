# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45
# para viagens mais longas. 

distancia = int(input('Insira a distancia em km: '))

if(distancia <= 200):   
    preco = 0.5 * distancia
else:
    preco = 0.45 * distancia

print('o preço dessa viagem é R$', preco)


