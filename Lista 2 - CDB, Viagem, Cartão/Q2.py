# Cartão de Crédito (Rotativo)

# Cartão de crédito é um produto financeiro que permite aos seus usuários realizarem
# compra a prazo em duas modalidades: 1) a vista: todo o valor vem na próxima
# fatura; e 2) parcelado: o valor é dividido em N parcelas/faturas.
# Em um dia fixo de cada mês previamente acordado é apurado todas as compras do
# período (30 dias) "à vista" e "parcelado" para gerar Fatura Mensal.
# Os cartões de crédito apesar de terem uma Bandeira (VISA, MASTER, ELO,
# CREDISHOP), são emitidos por Bancos. E são eles que recolhem também os
# pagamentos das faturas mensais.
# As faturas geralmente podem ser pagas total ou parcialmente. Os bancos definem
# um valor mínimo que deve ser pago para evitar bloqueio do cartão para novas
# compras. Quando o cliente paga o total da fatura não há incidência de Multas e/ou
# Juros sobre o valores das compras. Porém quando o pagamento for inferior ao Total
# será aplicado sobre o valor não pago Multas e Juros.
# No caso acima, nos próximos 30 dias serão acrescidos sobre o Saldo Devedor
# (valor não pago) o seguinte:
# - Juros do rotativo: geralmente um valor alto, como 12% a.m, a depender dos
# bancos.
# - Multa por atraso: Valor de aproximadamente 2% a.m.
# - Juros de mora: geralmente 1% a.m.
# Caso o pagamento seja inferior ao mínimo, além de Juros e Multas, o Cartão de
# Crédito fica bloqueado para novas compras, mesmo que ainda exista limite
# disponível.
# Considerando isso, faça um Simulador de Fatura de Cartão de Crédito, como
# seguinte cenário:
# 1) A pessoa usou o cartão de crédito em um único mês para várias compras e
# gerou uma fatura em um valor N reais. Peça ao usuário o valor total da fatura.
# 2) Permita simular duas opções de pagamento P1 e P2, que pode ser o valor
# total ou qualquer valor inferior a ele. Cada Plano P significa um Valor a Pagar
# e uma quantidade de meses sem pagar a fatura.
# 3) Em seguida, considere que o usuário ficou M meses sem pagar novamente a
# fatura (o saldo devedor ficou acumulando juros mes a mes);
# 4) Compute qual o valor da fatura (ou seja, o quanto ela cresceu) ao final dos M
# meses, no dois cenários de pagamento
# 5) Detalhe o valor original que gerou a dívida, e em quanto ela ficou. Mostre em
# quantos % a fatura cresceu nos dois cenários de pagamento.

def pagamento_inteiro(valor, pagamento):
    valor - pagamento == 0
    return 0


def pagamento_inferior(valor, pagamento):
    valor_restante = valor - pagamento
    return valor_restante


# Usaremos Juros Simples para calcular o juro da fatura
def juros_fatura(valor_restante, meses):
    montante = valor_restante + (valor_restante * 12/100 * meses) + (valor_restante * 2/100 * meses) + (valor_restante * 1/100 * meses)
    return montante


def computar_fatura(montante, valor):
    porcentagem = (montante * 100) / valor
    crescimento = porcentagem - 100
    return crescimento

valor_fatura = float(input('Digite o valor da fatura: '))

# Primeiro cenário, pagemento inteiro
pago = float(input('Digite o pagamento da fatura(completo): '))

completo = pagamento_inteiro(valor_fatura, pago)
print(f'Fatura paga, total restante a pagar R${completo}')

# Segundo cenário, pagamento inferior e juro
pago_inferior = float(input('Digite o pagamento da fatura(inferior): '))

inferior = pagamento_inferior(valor_fatura, pago_inferior)
print(f'Valor pago inferior, resta a pagar R${inferior}')

meses = int(input('Digite a quantidade de meses não pago: '))

fatura_juros = juros_fatura(inferior, meses)
crescimento = computar_fatura(fatura_juros,valor_fatura)
print('\n---------------------------------------------------------------')

print(f'Fatura atrasada com juros, valor R${fatura_juros} durante {meses} meses')
print(f'O crescimento do valor inicial de R${valor_fatura} para R${fatura_juros} é de {crescimento}%')
