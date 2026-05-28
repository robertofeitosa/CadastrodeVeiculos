from .adicionarmultaoveiculo import *

cadastro_veiculos = []

def cadastroveiculo():
    modelo = input("Digite o modelo do carro: ")
    print('')
    placa = input("Digite a placa do carro: ")
    print('')
    uf = input('Qual a UF do seu veiculo: ')
    print('')
    marca = input('Qual a marca do veiculo: ')
    print('')
    ano = input('Qual o ano do veiculo: ')
    print('')
    quilometragem = input('Qual a quilometragem do veiculo: ')
    print('')

    multas = []

    possui_multa = input('Veiculo possui alguma multa? [s] / [n]: ')
    print('')

    if possui_multa == 's':
        multas.append(multadoveiculo())
        while True:
            opcao = input('Deseja adicionar mais alguma multa? [s] / [n]: ')
            if opcao == 's':
                multas.append(multadoveiculo())
            elif opcao == 'n':
                break
            else:
                print('Opcao invalida...')
    else:
        print('Prossiga...')

    print('')
    veiculo = [modelo, placa, uf, marca, ano, quilometragem, multas]
    cadastro_veiculos.append(veiculo)
