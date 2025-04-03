# 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

# Entrada
valor = float(input('Digite um valor qualquer em R$: '))

# Processamento
novo_valor = (valor * 70) / 100

# Saída 
print(f'70% do R${valor:.2f} é R${novo_valor:.2f}')
