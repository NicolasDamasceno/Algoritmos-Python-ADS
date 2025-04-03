# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e
# ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
# d = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)

# Entrada
print('D = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)')
print('Digite abaixo 2 pontos quisquer em um plano (x1,x2) e (y1,y2)')
x1 = int(input('Digite um x1 inteiro: '))
x2 = int(input('Digite um x2 inteiro: '))

y1 = int(input('Digite um y1 inteiro: '))
y2 = int(input('Digite um y2 inteiro: '))

# Processamento
d = ((x2 - x1)**2 + (y2-y1)**2)**(1/2)

# Saída
print(f'O resultado da equação D = {d:.2f}')