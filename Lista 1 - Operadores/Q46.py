# 46. Uma loja vende seus produtos no sistema entrada mais duas prestações, sendo a entrada maior ou igual a
# cada uma das duas prestações; estas devem ser iguais, inteiras e as maiores possíveis. Por exemplo, se o
# valor da mercadoria for R$ 270,00, a entrada e as duas prestações são iguais a R$ 90,00; se o valor da
# mercadoria for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00.
# Escreva um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das duas
# prestações, de acordo com as regras acima.

# Entrada
valor = float(input('Digite o valor do produto em R$: '))

# Processamento
parcela = valor // 3
entrada = (valor % 3) + parcela

# Saída
print('---- Resumo da Compra ----')
print(f'Valor do Produto: R${valor:.2f}')
print(f'Valor da Entrada: R${entrada:.2f}')
print(f'Valor da Parcela em 2x: R${parcela:.2f}')