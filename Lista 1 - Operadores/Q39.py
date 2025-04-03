# 39. Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# D = (R + S) / 2, onde R = (A + B)**2 e S = (B + C)**2

# Entrada
print('D = (R + S) / 2, onde R = (A + B)**2 e S = (B + C)**2\n')
numA = int(input('Digite um A número inteiro e positivo: '))
numB = int(input('Digite um B número inteiro e positivo: '))
numC = int(input('Digite um C número inteiro e positivo: '))

# Processamento
r = (numA + numB)**2
s = (numB + numC)**2

d = (r + s)/2

# Saída
print(f'O resultado da equacão D é {d}')
