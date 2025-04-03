# 37. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# Entrada
idade_total_dias = int(input('Digite a sua idade em dias apenas: '))

# Processamento
anos = idade_total_dias // 365
meses = (idade_total_dias % 365) // 30
dias = (idade_total_dias % 365) % 30

# Saída
print(f'A sua idade é {anos} anos, {meses} meses e {dias} dias')
