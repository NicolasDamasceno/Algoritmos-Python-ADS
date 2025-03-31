# Conversão de minutos para horas e minutos
# Escreva um programa que converta minutos para horas e minutos.
# Entrada     Saída Esperada
#   125         2 hora(s) e 5 minuto(s)
#   90          1 hora(s) e 30 minuto(s)
#   200         3 hora(s) e 20 minuto(s)

# Entrada
entrada_minutos = int(input('Digite os minutos: '))

# Processamento
horas = entrada_minutos // 60

minutos_restantes = entrada_minutos % 60

# Saída
print(f'{entrada_minutos} são {horas} hora(s) e {minutos_restantes} minuto(s)')
