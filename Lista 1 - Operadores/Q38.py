# 38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

import fractions
# Usaremos o módulo fractions para realizar a soma e exibir o resultado
# Entrada
numerador1 = int(input('Digite o numerador da 1 fração: '))
denominador1 = int(input('Digite o denomindor da 1 fração: '))

numerador2 = int(input('Digite o numerador da 2 fração: '))
denominador2 = int(input('Digite o denomindor da 2 fração: '))

# Processamento
soma = fractions.Fraction(numerador1,denominador1) + fractions.Fraction(numerador2,denominador2)



# Saída
print(f'A soma das frações {numerador1}/{denominador1} + {numerador2}/{denominador2} é igual {soma}')