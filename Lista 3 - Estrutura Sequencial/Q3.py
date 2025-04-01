# 3. Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.

# Entrada
minutos = int(input('Digite os minutos: '))

# Processamento
horas = minutos // 60
minutos_restantes = minutos % 60

# Saída
print(f'Os minutos {minutos} equivalem a {horas}h e {minutos_restantes}min')