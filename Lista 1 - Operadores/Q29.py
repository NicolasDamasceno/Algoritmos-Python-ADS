# 29. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# Entrada
meses = int(input('Digite um valor inteiro de meses: '))

# Processamento
anos = meses // 12
meses_restantes = meses % 12

# Saída
print(f'{meses} meses equivale a {anos} anos e {meses_restantes} meses')