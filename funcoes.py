#####APRESENTAÇÃO#####
def linha(a = '', b = 0):
    print('{}{}{}'.format('\033[37m', a, '\033[m') * b)

def apresentacao():
    linha('=', 40)
    print(f'{"Mercado São Sebastião" :^40}')
    linha('=', 40)

def usuario():
    while True:
        print('[1] Gerente')
        print('[2] Caixa')
        try:
            escgc = input('Digite a sua opção: ')
            int(escgc)
        except ValueError:
            print('\033[31mDigite um valor válido!\033[m')
            continue
        else:
            escgc = int(escgc)
        linha('-', 40)
        if escgc == 1:
            apresentacao_gerente()
        elif escgc == 2:
            pass
        else:
            print('Digite uma opção válida')

#####GERENTE#####
def apresentacao_gerente():
    print(f'{"\033[32mSeja muito bem vindo Gerente!\033[m":^48}')
    validacao()

def validacao():
    while True:
        senha = str(input('Apenas precisamos validar a sua senha de acesso.\n\033[37m[Digite sair para voltar]\033[m\nDigite sua senha: ')).strip()
        if senha == 'Gerencia2389':
            print('\033[32mSenha correta\nEntrando no sistema\033[m')
            sistema_gerente()
            break
        elif senha.lower() == 'sair':
            print('Voltando!')
            linha('=', 40)
            break
        else:
            print('Senha Incorreta!')

def sistema_gerente():
    print('[1] Adicionar Produto')
    print('[2] Modificar Produto')
    print('[3] Modificar Quantidade de produtos')
    print('[4] Ver produtos')
    print('[5] Sair')
#####CAIXA#####

