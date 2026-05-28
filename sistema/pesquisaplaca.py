from .cadastrarveiculo import *

def pesquisarporplaca():
    placapesquisar = input('Digite a placa que deseja procurar: ')
    encontrado = False
    for veiculo in cadastro_veiculos:
        if veiculo[1] == placapesquisar:
            encontrado = True
            print('')
            print(f'O veiculo que voce procura e um: \033[31m{veiculo[0]} \033[m')
            print('')
            print(f'A Unidade Federativa do veiculo e: \033[31m{veiculo[2]} \033[m')
            print('')
            print(f'A marca do veiculo e: \033[31m{veiculo[3]} \033[m')
            print('')
            print(f'O ano do veiculo e: \033[31m{veiculo[4]} \033[m')
            print('')
            print(f'A quilometragem do veiculo e: \033[31m{veiculo[5]} \033[m')
            print('')
            print(f'O numero de multas desse veiculo e: \033[31m{len(veiculo[6])}\033[m')
            print('')
    if encontrado == False:
        print('Veiculo nao encontrado.')
