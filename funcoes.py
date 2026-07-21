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
        print('[3] Fechar')
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
        elif escgc == 3:
            print('Saindo do sistema!')
            linha('-', 40)
            break
        else:
            print('Digite uma opção válida')

def moeda():
    while True:
        try:
            valor = str(input('Digite o valor do produto: ')).strip().replace(',', '.')
            float(valor)
        except (ValueError):
            print('Digite um valor correto!')
            continue
        else:
            return float(valor)

def encontrar_produto(nome = ''):
    encontrado = False
    with open('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            if linha.strip().split(';')[0] == nome:
                encontrado = True
                break
        return encontrado

def modificar_produto(nome = ''):
    if encontrar_produto(nome):
        with open('produtos.txt', 'r') as arquivo:
            save = arquivo.readlines()
        for indice, linhap in enumerate(save):
            dados = linhap.strip().split(';')
            if dados[0] == nome:
                print(f'{"Produto":<15}{"Quantidade":<15}{"Preço"}')
                print(f'{dados[0]:<15}{dados[2]:<15}R${dados[1].replace(".", ",")}')
                linha('-', 40)
                print(f'{"O que gostaria de modificar":^40}')
                print('[1] Preço')
                print('[2] Quantidade de Produtos')
                while True:
                    try:
                        escpq = int(input('Digite a sua escolha: '))
                    except(ValueError):
                        print('\033[31mDigite um número válido!\033[m')
                    else:
                        break
                if escpq == 1:
                    dados[1] = str(moeda())
                elif escpq == 2:
                    dados[2] = str(int(input('Digite a quantidade do produto: ')))
                else:
                    print('Digite uma opção válida!')
                print('Produto Atualizado com sucesso!')
                linha('=', 40)
                save[indice] = ';'.join(dados) + '\n'
        with open('produtos.txt', 'w') as arquivo:
            arquivo.writelines(save)

#####GERENTE#####
def apresentacao_gerente():
    print(f'{"\033[32mSeja muito bem vindo Gerente!\033[m":^48}')
    validacao()

def validacao():
    while True:
        senha = str(input('Apenas precisamos validar a sua senha de acesso.\n\033[37m[Digite sair para voltar]\033[m\nDigite sua senha: ')).strip()
        if senha == 'Gerencia2389':
            print('\033[32mSenha correta\nEntrando no sistema\033[m')
            linha('=', 40)
            sistema_gerente()
            break
        elif senha.lower() == 'sair':
            print('Voltando!')
            linha('=', 40)
            break
        else:
            print('\033[31mSenha Incorreta!\033[m')

def sistema_gerente():
    while True:
        print('[1] Adicionar Produto')
        print('[2] Modificar Produto')
        print('[3] Modificar Quantidade de produtos')
        print('[4] Ver produtos')
        print('[5] Voltar')
        esc = int(input('Digite a sua escolha: '))
        linha('=', 40)
        if esc == 1:
            adicionando_produto()
        elif esc == 2:
            modificar_produto_gerencia()
        elif esc == 3:
            pass
        elif esc == 4:
            pass
        elif esc == 5:
            print('\033[32mVoltando o sistema! Volte Sempre!\033[m')
            linha('-', 40)
            break

def adicionando_produto():
    with open("produtos.txt", 'a') as arquivo:
        produto = {}
        produto['nome'] = str(input('Digite o nome do produto: ')).strip().title()
        if not encontrar_produto(produto['nome']):
            produto['preço'] = moeda()
            produto['quantidade'] = int(input('Digite a quantidade do produto: '))
            arquivo.write(f'{produto["nome"]};{produto["preço"]};{produto["quantidade"]}\n')
            print('Produto Adicionado com sucesso!')
            linha('=', 40)
        else:
            print('Esse produto já foi adicionado!')
            linha('=', 40)

def modificar_produto_gerencia():
    produto = {}
    produto['nome'] = str(input('Digite o nome do produto: ')).strip().title()
    if encontrar_produto(produto['nome']):
        modificar_produto(produto['nome'])
    else:
        print('Produto não encontrado!')

#####CAIXA#####

