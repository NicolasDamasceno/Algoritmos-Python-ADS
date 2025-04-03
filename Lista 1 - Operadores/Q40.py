# 40. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele
# fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

# Entrada
anos = int(input('Digite há quantos anos a pessoa fuma: '))
num_cigarro = int(input('Digite quantos cigarros são consumidos por dia: '))
preco_carteira = float(input('Digite o preço da carteira: '))

# Processamentos
total_cigarros = (anos * 365) * num_cigarro

num_carteiras = total_cigarros // 20

valor_gastos = num_carteiras * preco_carteira

# Saída
print(f'---- Dados do Fumantes ----')
print(f'Quantidade de cigarros fumados durante {anos} anos: {total_cigarros}')
print(f'Quantidade de carteira totais: {num_carteiras}')
print(f'Valor gasto ao longo de {anos} anos: R${valor_gastos:.2f}')