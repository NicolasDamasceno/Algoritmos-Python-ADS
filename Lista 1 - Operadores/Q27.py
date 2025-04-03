# 27. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

# Entrada
segundos = int(input('Digite um valor inteiro de segundos: '))

# Processaento
horas = segundos // 3600

minutos = (segundos % 3600) // 60

segundos_restantes = (segundos % 3600) % 60

# Saída
print(f'{segundos}s equivale a {horas}h, {minutos}min e {segundos_restantes}s')