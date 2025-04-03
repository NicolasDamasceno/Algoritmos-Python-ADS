# 25. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

# Entrada
m = int(input('Digite um valor inteiro em m: '))

# Processamento
km = m / 1000

km_m = m / km

# Saída
print(f'{m}m equivale a {km}km')
print(f'Os {km}km correspondem a {km_m} metros')
