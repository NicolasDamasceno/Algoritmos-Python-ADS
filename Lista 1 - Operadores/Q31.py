# 31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

# Entrada
binario = int(input('Digite um número binário de 4 dígitos: '))

# Processamento
# Leremos o número Binário da esquerda para direita
# Separando os dígitos
digito1 = binario // 1000
digito2 = (binario % 1000) // 100
digito3 = ((binario % 1000) % 100) // 10
digito4 = ((binario % 1000) % 100) % 10

# Transformando de binário para decimal
decimal = (digito1 * (2)**3) + (digito2 * (2)**2) + (digito3 * (2)**1) + (digito4 * 1) 

# Saída
print(f'O binário {binario} na base decimal é {decimal}')
