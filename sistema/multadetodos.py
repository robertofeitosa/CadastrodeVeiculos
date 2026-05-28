from .cadastrarveiculo import *

def multa_degeral():
    for veiculo in cadastro_veiculos:
        multas = veiculo[6]
        print('')
        print(f'O veiculo e um: \033[31m{veiculo[0]} \033[m')
        print('')
        print(f'A placa do veiculo e: \033[31m{veiculo[1]} \033[m')
        print('')
        print(f'O numero de multas desse veiculo e: \033[31m{len(multas)}\033[m')
        print('')

        for multa in multas:
            print(f'Data: {multa[0]}')
            print(f'Cidade: {multa[1]}')
            print(f'Valor: {multa[2]}')
            print('')
