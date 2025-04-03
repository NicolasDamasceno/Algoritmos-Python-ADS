# 11. Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

# Entrada
num = int(input('Digite um número inteiro com 3 dígitos: '))

# Processamento 
centana = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10


# Saída
print(f'O inverso dos dígitos de {num} é {unidade}{dezena}{centana}')