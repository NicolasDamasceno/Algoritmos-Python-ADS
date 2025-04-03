# 35. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.: número = 9534 ; soma = 9+5+3+4 = 21.

# Entrada
num = int(input('Digite um número inteiro de 4 dígitos: '))

# Processamento
milhar = num // 1000
centena = (num % 1000) // 100
dezena = ((num % 1000) % 100) // 10
unidade = ((num % 1000) % 100) % 10

soma = milhar + centena + dezena + unidade

# Saída
print(f'A soma dos elementos de {num} é {soma}')
