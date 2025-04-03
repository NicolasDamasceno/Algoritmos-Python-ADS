# 36. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

# Entrada
idade_ano = int(input('Digite a sua idade em anos: '))
idade_mes = int(input('Digite o restante dela em meses: '))
idade_dia = int(input('Digite o restante dela em dias: '))

# Processamento
idade_dias_total = (idade_ano * 365) + (idade_mes * 30) + idade_dia

# Saída
print(f'A sua idade em dia é {idade_dias_total} dias')
