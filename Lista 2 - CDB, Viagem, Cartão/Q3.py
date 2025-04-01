# 3. Viagem de Férias

# Uma família comprou um carro híbrido (Elétrico e a Combustão) de uma marca de
# veículos chamada (Mercedes). Quando em uso do Motor Elétrico não
# há qualquer consumo de combustível (Gasolina Comum/Aditivada ou Álcool). Já
# quando em Motor a combustão: o consumo de energia elétrica também será zero,
# pois faz uso de alternador ligado ao motor mecânico para gerar energia elétrica para
# dispositivos como Vidros, Elétricos, Ar Condicionado e etc.
# A viagem de feriadão da família tá chegando e estão fazendo o planejamento da
# viagem quanto a combustível e valores gastos para isso.
# Para o motor a combustão: o consumo de combustível é por km/litro, ou seja,
# geralmente um veículo roda entre 10 e 15 km com 1 litro de gasolina. Quando é
# abastecido com Álcool o consumo é, em média, 80% disso, ou seja, 8 a 12 km/L.
# Já o motor elétrico o consumo é também por km. Ou seja, uma bateria que abastece
# o motor, quando 100% carregada, tem N Km de autonomia, em média/estimativa.
# Sobre os valores (R$) envolvidos os custos são (EXEMPLO: R$ 5,99 o litro
# gasolina, R$ 4,12 o litro do álcool, já no caso de bateria considere que o
# abastecimento é feito por meio de pontos gratuítos como em Estacionamentos de
# Supermercado ou Empresas de Energia Solar, como podemos encontrar em
# grandes Capitais como Teresina)
# Considere que sempre conseguiria abastecer tanto a bateria quanto o tanque de
# combustível durante a viagem. E que por motivos quaisquer como tipo de rodovia,
# trechos urbanos ou descarga, será necessário usar o motor a combustão em
# alguma fatia da viagem apesar do motor elétrico ser de custo Zero.
# Peça ao usuário qual a distância percorrida total prevista para viagem. Em seguida,
# pergunte qual o valor do Litro do Álcool e Gasolina. Solicite também qual o
# percentual da viagem que ele deve conseguir usando o Motor Elétrico.
# Seu programa deve informar quanto ele precisará abastecer (litros e R$) com Álcool
# ou com Gasolina para poder completar a viagem. Ele irá usar apenas álcool ou
# gasolina, porém você deve mostrar os dois cenários, se for com álcool precisará de
# N R$ e L litros, e a mesma coisa com gasolina.
# Apresente a tabela comparativa para o usuário.

# Consideremos que o carro fará na estrada 15km/L na gasolina 
def litros_gasolina(distancia):
    litros = distancia / 15
    return litros


def valor_gasolina(preco, litros):
    valor = preco * litros
    return valor


# Consideremos que o carro fará na estrada 12km/L no álcool
def litros_alcool(distancia):
    litros = distancia / 12
    return litros


def valor_alcool(preco, litros):
    valor = preco * litros
    return valor

def percentual_eletrico(distancia_total, percentual):
    distancia_percentual = (distancia_total * percentual) / 100

    return distancia_percentual

# Realizando os cálculos 
distancia_total = int(input('Digite a distância total em Km: '))
motor_eletrico = int(input('Digite o percentual que o motor eletrico irá percorrer(%): '))
print('')
preco_gasolina = float(input('Digite o valor da Gasolina(R$): '))
preco_alcool = float(input('Digite o valor do Álcool(R$): '))
print('')
distancia_eletrica = percentual_eletrico(distancia_total, motor_eletrico)

distancia_restante = distancia_total - distancia_eletrica

gasolina_litros_total = litros_gasolina(distancia_restante)
gasolina_valor_total = valor_gasolina(preco_gasolina, gasolina_litros_total)

alcool_litros_total = litros_alcool(distancia_restante)
alcool_valor_total = valor_alcool(preco_alcool, alcool_litros_total)

print('------> Comparação entre Gasolina e Álcool <-----')
print(f'Distancia total: {distancia_total:.1f}Km')
print(f'Distancia percorrida pelo motor elétrico: {distancia_eletrica:.1f}Km')
print(f'Distancia restante: {distancia_restante:.1f}Km\n')

print(f'Para pecorrer os Km restantes na Gasolina: \n{gasolina_litros_total:.1f}L de Gasolina\nR${gasolina_valor_total:.2f}')
print('')
print(f'Para pecorrer os Km restantes no Álcool: \n{alcool_litros_total:.1f}L de Álcool\nR${alcool_valor_total:.2f}')


