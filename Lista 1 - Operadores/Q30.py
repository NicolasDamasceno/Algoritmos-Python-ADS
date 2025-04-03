# 30. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos elecorresponde.

# Entrada
minutos = int(input('Digite um valor inteiros de minutos: '))

# Processamento
dias = minutos // 1440
horas = (minutos % 1440) // 60
minutos_restantes = (minutos % 1440) % 60

# Saída
print(f'{minutos}min equivale a {dias} dias, {horas}h e {minutos_restantes}min')