# 26. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# Entrada
dias = int(input('Digite um números inteiros de dias: '))

# Processamento 
semanas = dias // 7
dias_restantes = dias % 7

# Saída
print(f'{dias} dias equivalem a {semanas} semanas e {dias_restantes} dias')
