# Cálculo do valor final de um produto com desconto
# Escreva um programa que aplique um desconto percentual sobre um preço inicial.
# Entrada   Saída Esperada
# 100 10        90.0
# 200 25        150.0
# 500 5         475.0

# Entrada
valor_inicial = int(input('Digite o valor do produto: '))

desconto = int(input('Digite o percentual do desconto: '))

# Processamento
valor_desconto = valor_inicial * (desconto/100)

valor_final = valor_inicial - valor_desconto

# Saída
print(f'O valor de R${valor_inicial} com {desconto}% é de R${valor_final:0.1f}')