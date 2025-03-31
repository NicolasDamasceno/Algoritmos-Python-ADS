# Média Ponderada
# Escreva um programa que calcule a média ponderada de três notas, considerando seus respectivos
# pesos.
# Entrada           Saída Esperada
# 8 2 7 3 6 5       6.7
# 10 4 5 2 8 4      8.2
# 3 1 7 1 10 2      7.5

# Entrada
nota1 = float(input('Digite a nota 1: '))
peso1 = int(input('Digite o peso da nota 1: '))

nota2 = float(input('Digite a nota 2: '))
peso2 = int(input('Digite o peso da nota 2: '))

nota3 = float(input('Digite a nota 3: '))
peso3 = int(input('Digite o peso da nota 3: '))


# Processamento
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Saída 
print(f'A média ponderada das notas é {media:0.1f}')
