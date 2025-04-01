# 2. Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

# Entrada
horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))

# Processamento
minutos_totais = (horas * 60) + minutos

# Saída
print(f'Os minutos totais são {minutos_totais}min')