# 41. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
# seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
# escreva o custo ao consumidor.

# Entrada
custo_fabrica = float(input('Digite o custo de fábrica em R$: '))

# Processamento
percentagem_distribuidor = custo_fabrica * (28/100)
impostos = custo_fabrica * (45/100)

custo_consumidor = custo_fabrica + percentagem_distribuidor + impostos

# Saída
print(f'\n---- Dados do custo do carro ----')
print(f'Custo de Fábrica: R${custo_fabrica:.2f}')
print(f'Percentual do Distribuidor: R${percentagem_distribuidor:.2f}')
print(f'Impostos: R${impostos:.2f}')
print(f'Custo para o Consumidor Final: R${custo_consumidor:.2f}')
