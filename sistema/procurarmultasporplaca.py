from .cadastrarveiculo import *

def multa_porplaca():   
    placa_pesquisa = input('Digite a placa do veículo: ')
    encontrado = False

    for veiculo in cadastro_veiculos:
        if veiculo [1] == placa_pesquisa:
            encontrado = True
            multas = veiculo[6]
            print('')
            print(f'Veiculo: \033[31m{veiculo[0]}\033[m')
            print(f'Placa: \033[31m{veiculo[1]}\033[m')
            print(f'Quantidade de multas: \033[31m{len(multas)}\033[m')
            print('')

            if len(multas) == 0:
                print ('Esse veículo nao possui multas.')
            else:
                for multa in multas:
                    print(f'Data: {multa[0]}')
                    print(f'Cidade: {multa[1]}')
                    print(f'Valor: {multa[2]}')
                    print('')

    if encontrado == False:
        print('Veiculo nao encontrado.')
