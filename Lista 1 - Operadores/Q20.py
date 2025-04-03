# 20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

# Entrada
celsius = int(input('Digite uma temperatura em C(celsius): '))

# Processamento
fahrenheit = (9 * celsius + 160) / 5

# Saída
print(f'{celsius}C equivale a {fahrenheit:.1f}F')