# 33. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.

# Entrada
num = int(input('Digite um número inteiro com 3 dígitos: '))

# Processamento
unidade = num // 100
dezena = (num % 100) // 10
centana = (num % 100) % 10

num_inverso = (centana * 100) + (dezena * 10) + unidade

soma = (num + num_inverso)

# Saída
print(f'A soma entre o {num} e o seu inverso {num_inverso} é {soma}')
