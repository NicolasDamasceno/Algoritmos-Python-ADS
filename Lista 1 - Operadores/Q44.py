# 44. Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
# quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada
# pelo usuário.

# Entrada
latao = float(input('Digite a quantidade de Latão requirida em Kg: '))

# Processamento
zinco = (30/100) * latao
cobre = (70/100) * latao

# Saída
print(f'\n---- Produção de Latão ----')
print(f'Quantidade de Latão requerida: {latao}Kg')
print(f'Quantidade de Zinco: {zinco:.2f}Kg')
print(f'Quantidade de Cobre: {cobre:.2f}Kg')