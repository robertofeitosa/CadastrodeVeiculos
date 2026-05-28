from .cadastrarveiculo import *

def listarveiculos():
    for a in cadastro_veiculos:
        print('')
        print(f'O modelo do veiculo e: \033[31m{a[0]}\033[m')
        print('')
        print(f'A placa do veiculo e: \033[31m{a[1]}\033[m')
        print('')
        print(f'A UF do veiculo e: \033[31m{a[2]}\033[m')
        print('')
        print(f'A marca do veiculo e: \033[31m{a[3]}\033[m')
        print('')
        print(f'O ano do veiculo e: \033[31m{a[4]}\033[m')
        print('')
        print(f'A quilometragem do veiculo e: \033[31m{a[5]}\033[m')
        print('')
        print(f'Seu veiculo possui \033[31m{len(a[6])}\033[m multas.')
        print('')
