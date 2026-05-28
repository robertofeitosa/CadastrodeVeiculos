from .cadastrarveiculo import *

def quilometro():
    km = input('Digite quantos km do veiculo que esta a procura: ')
    encontrado = False
    for veiculo in cadastro_veiculos:
        if veiculo[5] == km:
            encontrado = True
            print('')
            print(f'O veiculo que voce procura e um: \033[31m{veiculo[0]} \033[m')
            print('')
            print(f'A Unidade Federativa do veiculo e: \033[31m{veiculo[2]} \033[m')
            print('')
            print(f'A marca do veiculo e: \033[31m{veiculo[3]} \033[m')
            print('')
            print(f'A placa do veiculo e: \033[31m{veiculo[1]} \033[m')
            print('')
            print(f'O ano do veiculo e: \033[31m{veiculo[4]} \033[m')
            print('')
            print(f'O numero de multas desse veiculo e: \033[31m{len(veiculo[6])}\033[m')
            print('')
    if encontrado == False:
        print('Veiculo nao encontrado.')
