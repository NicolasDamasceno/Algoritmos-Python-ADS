# Número invertido de três dígitos
# Escreva um programa que receba um número de três dígitos e exiba ele invertido.
# Entrada   Saída Esperada
#   123         321
#   450         54
#   987         789

# Entrada
# Obs: Não usaremos a função reverse
num = int(input('Digite um número intreiro com três dígitos: '))

# Processamento
ultimo_digito = num // 100
meio_digito = (num % 100) // 10
primeiro_digito = (num % 100) % 10

num_invertido = (primeiro_digito * 100) + (meio_digito * 10) + (ultimo_digito)

# Saída
print(f'O inverso de {num} é {num_invertido}')