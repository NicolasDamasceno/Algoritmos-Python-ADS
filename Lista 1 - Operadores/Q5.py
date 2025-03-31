# Troco com notas de 50 e 10
# Escreva um programa que determine a quantidade de notas de 50 e 10 necessárias para um
# determinado valor.
#   Entrada     Saída Esperada
#     130           2 nota(s) de 50 e 3 nota(s) de 10
#      70           1 nota(s) de 50 e 2 nota(s) de 10
#      90           1 nota(s) de 50 e 4 nota(s) de 10

# Entrada
valor = int(input('Digite o valor inteiro a ser sacado: '))

# Processamento
notas_50 = valor // 50

notas_10 = (valor % 50) // 10

# Saída
print(f'{notas_50} de 50 e {notas_10} nota(s) de 10')