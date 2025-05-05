from in_onputs import obter_numero_inteiro
# 25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
# uma mensagem de permissão de acesso ou não.
def verificar_senha(senha):
    verificado = 1234
    if senha == verificado:
        return True
    return False

def main():
    senha_digitada = obter_numero_inteiro('Digite a senha: ')
    if verificar_senha(senha_digitada):
        print('Senha correta!')
    else:
        print('Senha incorreta, tente novamente...')

if __name__ == '__main__':
    main()