# 1. CDB e CDC

# Leia, Interprete e faça um simulador para o seguinte problema (Contexto Adaptado).
# Os bancos captam dinheiro para suas operações por meio de CDBs (Certificado de
# Depósito Bancário), dentre outras formas. Por outro lado, eles fazem empréstimos
# aos seus clientes em operações ditas CDC (Crédito Direto ao Consumidor).
# Para o CDB o cliente do Banco receberá uma recompensa pelo investimento com
# taxa de juros sobre valor entre 1% e 20% (ao ano), por exemplo, aplicada em Juros
# Compostos (desconsidere IR - Imposto de Renda).
# Já o CDC é um valor percentual geralmente entre 1% e 17% (ao mês), a depender do
# tipo do empréstimo, em Juros Compostos. O Cliente paga o CDC mensalmente em
# parcelas iguais. Os prazos comuns são 24x, 36x e até 60x.
# O Lucro do Banco é o Juros dos Empréstimos descontado o quanto ele pagará de
# Juros para os Investidores de CDB. Considerando as afirmações acima, faça um
# SIMULADOR de CDB e em conjunto um Simulador de CDC (Empréstimo) do mesmo
# valor captado. Para o CDB, solicite os dados necessários, identifique quais pelo
# contexto.
# Em seguida, calcule quanto o Banco irá pagar (Valor Investido + Juros CDB) para o
# Investidor ao final do período escolhido. Exemplo: Um CDB de vencimento 2035, tem
# um prazo de 10 anos. 2035 - 2025.
# Já no empréstimo, pergunte os demais dados necessários para simular um
# empréstimo e mostre quanto o Cliente CDC irá pagar de Juros ao todo para o Banco.
# Mostre também o valor das Parcelas. E o montante total a pagar.
# Por fim, faça um resumo sobre o Lucro do Banco com as transações de CDB e CDC.
# Incluindo todos os dados das duas operações.

# Modularização
 
# Tempo é em anos
# O juros será fixo ao 8% anual
def cdb(capital, anual):
    montante = capital * ((1 + 8/100) ** anual)
    
    return montante

# Tempo é em meses
def cdc(capital, juros, mensal):
    montante = capital * ((1 + juros/100) ** mensal)

    return montante

# Entrada

# O cliente fez uma operação CDB, com capital de R$1000 com juros de 8% ao ano e com prazo de 10 anos (2025-2035)
cliente = cdb(1000, 10)

# O banco simulou um empréstismo CDC, com capital de R$1000 com juros de 10% ao mês e com prazos de 24x, 36x e 60x meses
banco_24 = cdc(1000, 10, 24)
banco_36 = cdc(1000, 10, 36)
banco_60 = cdc(1000, 10, 60)

# Processamento
parcelas_24 = banco_24 / 24
parcelas_36 = banco_36 / 36
parcelas_60 = banco_60 / 60

lucro_24 = banco_24 - cliente
lucro_36 = banco_36 - cliente
lucro_60 = banco_60 - cliente

# Saída
print(f'Operação CDB: R${cliente:.2f} com juros de 8%')
print('---------------------------------------------------\n')
print('Simulação de Empréstismo em CDC a juros de 10%')
print(f'Empréstimo de R$1000 em x24 de R${parcelas_24:.2f}, total R${banco_24:.2f}')
print(f'Empréstimo de R$1000 em x36 de R${parcelas_36:.2f}, total R${banco_36:.2f}')
print(f'Empréstimo de R$1000 em x60 de R${parcelas_60:.2f}, total R${banco_60:.2f}')
print('---------------------------------------------------\n')
print('Lucro do Banco')
print(f'Lucro com 24x parcelas: R${lucro_24:.2f}')
print(f'Lucro com 36x parcelas: R${lucro_36:.2f}')
print(f'Lucro com 60x parcelas: R${lucro_60:.2f}')
print('---------------------------------------------------\n')
