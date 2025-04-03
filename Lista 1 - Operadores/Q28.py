# 28. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas elecorresponde.

# Entrada
horas = int(input('Digite um número inteiros de horas: '))

# Processamentos
semanas = horas // 168
dias = (horas % 168) // 24
horas_restantes = (horas % 168) % 24

# Saída
print(f'{horas}h equivale a {semanas} semanas, {dias} dias e {horas_restantes}h')
