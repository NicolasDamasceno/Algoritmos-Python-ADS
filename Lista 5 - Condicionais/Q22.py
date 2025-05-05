from in_onputs import obter_numero_inteiro
# 22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
# hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
# seguinte.

def duracao_jogo(hora_inicio, min_inicio, hora_final, min_final):
    min_total_inicio = (hora_inicio * 60) + min_inicio
    min_total_final = (hora_final * 60) + min_final

    if min_total_final < min_total_inicio:
        min_total_final += 24 * 60

    min_duracao = min_total_final - min_total_inicio

    hora_duracao = min_duracao // 60
    min_duracao = min_duracao % 60

    return hora_duracao, min_duracao

def main():
    hora_inicio = obter_numero_inteiro('Digite a hora inicial: ')
    min_inicio = obter_numero_inteiro('Digite os minutos inicial: ')
    hora_final = obter_numero_inteiro('Digite a hora final: ')
    min_final = obter_numero_inteiro('Digite os minutos final: ')
    hora_duracao, min_duracao = duracao_jogo(hora_inicio, min_inicio, hora_final, min_inicio)
    print('\n-----> Tempo do Jogo <-----')
    print(f'Horário de Ínicio: {hora_inicio}h {min_inicio}minutos\nHorário do Término: {hora_final}h {min_final}minutos')
    print(f'\nDuração total: {hora_duracao}h {min_duracao}minutos')

if __name__ == '__main__':
    main()