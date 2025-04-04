# Um sistema de equações lineares do tipo ax + by = c e dx + ey = f, pode ser resolvido segundo mostrado abaixo
# x = (ce - bf) / (ae - bd) e y = (af - cd) / (ae - bd)

# Entrada
a = int(input('Digite um número inteiro A: '))
b = int(input('Digite um número inteiro B: '))
c = int(input('Digite um número inteiro C: '))
d = int(input('Digite um número inteiro D: '))
e = int(input('Digite um número inteiro E: '))
f = int(input('Digite um número inteiro F: '))

# Processamento
x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

# Saída
print('\n---- Equação ----')
print('Equações lineares: ax + by = c e dx + ey = f')
print('Resolução x = (ce - bf) / (ae - bd) e y = (af - cd) / (ae - bd)\n')
print(f'O valor da equação X é {x}')
print(f'O valor da equação Y é {y}')