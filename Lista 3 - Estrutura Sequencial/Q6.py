# 6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

# Entrada
velocidade = float(input('Digite a velocidade em hm/h: '))

# Processamento
velocidade_ms = velocidade / 3.6

# Saída
print(f'A velocidade de {velocidade:.1f}km/h é {velocidade_ms:.1f}m/s')
