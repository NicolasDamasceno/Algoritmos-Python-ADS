# Cálculo do juros simples
# Escreva um programa que calcule o montante final em uma aplicação financeira com juros simples.
# Entrada       Saída Esperada
# 1000 0.02 6       1120.0
# 500 0.05 4        600.0
# 2000 0.01 12      2240.0

# Entrada
valor = int(input('Digite o valor da aplicação: '))

juros = float(input('Digite o percentual do juros: '))

tempo = int(input('Digite o tempo mensal: '))

# Processamento 
montante = valor + (valor * juros * tempo)

# Saída 
print(f'O Montante ao final de {tempo} meses é R${montante:0.1f}')