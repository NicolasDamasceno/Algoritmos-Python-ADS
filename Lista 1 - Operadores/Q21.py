# 21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).

# Entrada
fahrenheit = int(input('Digite uma temperatura em F(Fahrenheit): '))

# Processamento
celsius = (5 * fahrenheit - 160) / 9

# Saída
print(f'{fahrenheit:.1f}F equivale a {celsius:.1f}C')