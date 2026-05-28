from .cadastrarveiculo import *

def excluirveiculo():
    placa_pesquisar = input('Digite a placa do veículo que deseja excluir: ')

    for veiculo in cadastro_veiculos:
        if veiculo[1] == placa_pesquisar:
            print('')
            print(f'Modelo: {veiculo[0]}')
            print(f'Placa: {veiculo[1]}')
            print(f'UF: {veiculo[2]}')
            print(f'Marca: {veiculo[3]}')
            print(f'Ano: {veiculo[4]}')
            print('')

            confirmar = input('Tem certeza que deseja excluir este veículo? [s] / [n]: ')

            if confirmar == 's':
                cadastro_veiculos.remove(veiculo)
                print('Veículo excluído com sucesso!')
            else:
                print('Exclusão cancelada.')

            return

    print('Veículo não encontrado.')
