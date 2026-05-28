from .cadastrarveiculo import *
from .adicionarmultaoveiculo import *

def modificarveiculo():
    placa_pesquisa = input('Digite a placa do veiculo que deseja modificar: ')
    for veiculo in cadastro_veiculos:
        if veiculo[1] == placa_pesquisa:
            while True:
                print('')
                print('Veiculo encontrado:')
                print('')
                print(f'[1] - O modelo do veiculo e: \033[31m{veiculo[0]}\033[m')
                print('')
                print(f'[2] - A placa do veiculo e: \033[31m{veiculo[1]}\033[m')
                print('')
                print(f'[3] - A UF do veiculo e: \033[31m{veiculo[2]}\033[m')
                print('')
                print(f'[4] - A marca do veiculo e: \033[31m{veiculo[3]}\033[m')
                print('')
                print(f'[5] - O ano do veiculo e: \033[31m{veiculo[4]}\033[m')
                print('')
                print(f'[6] - A quilometragem do veiculo e: \033[31m{veiculo[5]}\033[m')
                print('')
                print(f'[7] - Seu veiculo possui \033[31m{len(veiculo[6])}\033[m multas.')
                print('')
                print('0 - Sair')
                print('')

                opcao = input('Qual informacao deseja modificar? ')

                if opcao == '1':
                    veiculo[0] = input('Digite o novo modelo: ')
                elif opcao == '2':
                    veiculo[1] = input('Digite a nova placa: ')
                elif opcao == '3':
                    veiculo[2] = input('Digite a nova UF: ')
                elif opcao == '4':
                    veiculo[3] = input('Digite a nova marca: ')
                elif opcao == '5':
                    veiculo[4] = input('Digite o novo ano: ')
                elif opcao == '6':
                    veiculo[5] = input('Digite a nova quilometragem: ')
                elif opcao == '7':
                    veiculo[6].append(multadoveiculo())
                elif opcao == '0':
                    print('Modificacao finalizada.')
                    return
                else:
                    print('Opcao invalida.')

                return

    print('Veiculo nao encontrado.')
