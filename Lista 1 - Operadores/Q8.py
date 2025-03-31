# Cálculo do IMC
# Escreva um programa que calcule o Índice de Massa Corporal (IMC), dado o peso e a altura.
# Entrada   Saída Esperada
# 70 1.75       22.86
# 90 1.80       27.78
# 50 1.60       19.53

# Entrada
peso = int(input('Digite o peso em kg: '))

altura = float(input('Digite a altura em m: '))

# Processamento
imc = peso / (altura * altura)

# Saída 
print(f'O IMC da pessoa é {imc:0.2f}')