# 19. Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)

# Entrda 
raio = float(input('Digite o raio em cm de uma esfera: '))

# Processamento
volume = (4 * 3.14 * raio**3) / 3

# Saída
print(f'O volume da Esfera com raio de {raio}cm é {volume:.1f}cm3')