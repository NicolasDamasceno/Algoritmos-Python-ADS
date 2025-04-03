# 12. Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

# Entrada 
salario = float(input('Digite o salário do trabalhador: '))

# Processamento
aumento = (salario * 25) / 100
novo_salario = salario + aumento

# Saída
print(f'Com o aumento de 25% o salário de R${salario:.2f} vai para R${novo_salario:.2f}')
