# 45. Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para
# decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o
# saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor
# disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de
# notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria
# indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um
# algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o
# critério da distribuição ótima.

# Entrada
valor_saque = int(input('Digite o valor(R$) desejado para o saque: '))

# Processamento
notas50 = valor_saque // 50
notas10 = (valor_saque % 50) // 10
notas5 = ((valor_saque % 50) % 10) // 5
notas1 = ((valor_saque % 50) % 10) % 5

# Saída
print('\n---- Caixa Eletrônico ----')
print(f'Valor Sacado: R${valor_saque}')
print(f'Quantidade de notas de R$ 50 é {notas50}')
print(f'Quantidade de notas de R$ 10 é {notas10}')
print(f'Quantidade de notas de R$ 5 é {notas5}')
print(f'Quantidade de notas de R$ 1 é {notas1}')