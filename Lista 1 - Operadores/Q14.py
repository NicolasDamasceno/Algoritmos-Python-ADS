# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

# Entrada 
nota1 = float(input('Digite a nota 1: '))
peso1 = int(input('Digite o peso da nota 1: '))

nota2 = float(input('Digite a nota 2: '))
peso2 = int(input('Digite o peso da nota 2: '))

nota3 = float(input('Digite a nota 3: '))
peso3 = int(input('Digite o peso da nota 3: '))

# Processamento
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Saída
print("---- Notas e Média ----")
print(f'Nota 1: {nota1:.1f}\nNota 2 : {nota2:.1f}\nNota 3: {nota3:.1f}\n')
print(f'Média: {media_ponderada:.1f}')