from .cadastrarveiculo import *

def pesquisaporuf():
    pesquisaruf = input('Digite a Unidade da Federacao do veiculo: ')
    encontrado = False
    for veiculo in cadastro_veiculos:
        if veiculo[2] == pesquisaruf:
            encontrado = True
            print('')
            print(f'Placa do veiculo: \033[31m{veiculo[1]} \033[m')
            print('')
            print(f'Modelo do veiculo: \033[31m{veiculo[0]} \033[m')
            print('')
            print(f'A marca do veiculo e: \033[31m{veiculo[3]}\033[m')
            print('')
            print(f'O ano do veiculo e: \033[31m{veiculo[4]}\033[m')
            print('')
            print(f'A quilometragem do veiculo e: \033[31m{veiculo[5]}\033[m')
            print('')
            print(f'Esse veiculo possui \033[31m{len(veiculo[6])}\033[m multas.')
            print('')
    if encontrado == False:
        print('Veiculo nao encontrado.')
