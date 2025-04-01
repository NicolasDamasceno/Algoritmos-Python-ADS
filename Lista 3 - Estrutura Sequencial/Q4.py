# 4. Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

# Entrada 
cotacao = float(input('Digite a cotação do dólar(U$) atual: '))
dolar = float(input('Digite um valor em dólar(U$): '))

# Processameto 
real = dolar * cotacao

# Saída 
print(f'U${dolar:.2f} equivale a R${real:.2f}')