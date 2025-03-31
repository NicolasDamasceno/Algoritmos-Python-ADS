# Cálculo de tempo de viagem
# Escreva um programa que calcule quanto tempo levará uma viagem, dado a distância e a
# velocidade média.
#   Entrada       Saída Esperada
#   300 100           3.0
#   150 50            3.0
#   600 120           5.0

# Entrada
# Usaremos a velocidade com km/h, logo o resultado será em h
distancia = int(input('Digite a distância em km: '))

velocidade = int(input('Digite a velocidade média: '))

# Processamento 
tempo = distancia / velocidade

# Saída
print(f'O tempo para pecorrer {distancia}km a {velocidade}km/h é {tempo:.1f}h')