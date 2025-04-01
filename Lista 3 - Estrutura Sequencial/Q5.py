# 5. Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).

# Entrada
num = int(input('Digite um número inteiro com 3 dígitos: '))

# Processamento 
centana = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10

soma = centana + dezena + unidade

# Saída
print(f'A soma dos dígitos de {num} é {soma}')