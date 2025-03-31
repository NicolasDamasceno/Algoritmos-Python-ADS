# Soma dos primeiros N números naturais
# Escreva um programa que calcule a soma dos primeiros N números naturais.
# Entrada       Saída Esperada
#   5                 15
#   10                55
#   100               5050

# Entrada
num = int(input('Digite um número natural: '))

# Processamento 
soma_par  = 1 + num

quantidade_par = (num - 1 + 1)/ 2

soma = soma_par * quantidade_par

# Saída
print(f'A soma dos primeiros {num} números naturais é {soma:.0f}') 