import os

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção: {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrando restaurante')
    elif opcao_escolhida == 2:
        print('Listando restaurante')
    elif opcao_escolhida == 3:
        print('Ativando restaurante')
    else:
        finalizar_app()

def finalizar_app():
    os.system('clear')
    print('Finalizando app')


def exibir_nome_do_programa():
    print('SABORES')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()