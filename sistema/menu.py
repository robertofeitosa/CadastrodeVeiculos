from .cadastrarveiculo import *
from .listarveiculos import *
from .pesquisaplaca import *
from .veiculosporuf import *
from .veiculoporano import *
from .adicionarmultaoveiculo import *
from .veiculoporkm import *
from .modificarveiculo import *
from .excluirporplaca import *
from .procurarmultasporplaca import *
from .multadetodos import *

def menu():
    while True:
        print('')
        print('[1] - CADASTRAR VEICULO...')
        print('')
        print('[2] - MODIFICAR VEICULO CADASTRADO POR PLACA...')
        print('')
        print('[3] - EXCLUIR VEICULO CADASTRADO POR PLACA...')
        print('')
        print('[4] - LISTAR TODOS OS VEICULOS INFORMADOS...')
        print('')
        print('[5] - PESQUISAR VEICULO POR PLACA...')
        print('')
        print('[6] - PESQUISAR TODOS OS VEICULOS POR UF...')
        print('')
        print('[7] - PESQUISAR TODOS OS VEICULOS POR ANO...')
        print('')
        print('[8] - LISTAR VEICULOS POR QUILOMETRAGEM...')
        print('')
        print('[9] - EXIBIR MULTAS DE VEICULOS POR PLACA...')
        print('')
        print('[10] - EXIBIR MULTAS DE TODOS OS VEICULOS CADASTRADOS...')
        print('')
        print('[11] - SAIR...')
        print('')

        try:
            opcao = int(input("Qual sua escolha? "))
        except ValueError:
            print('')
            print('\033[31mERRO NA APLICACAO, INSIRA UM NUMERO\033[m')
            print('')
            continue

        if opcao == 1:
            cadastroveiculo()
        elif opcao == 2:
            modificarveiculo()
        elif opcao == 3:
            excluirveiculo()
        elif opcao == 4:
            listarveiculos()
        elif opcao == 5:
            pesquisarporplaca()
        elif opcao == 6:
            pesquisaporuf()
        elif opcao == 7:
            pesquisaporano()
        elif opcao == 8:
            quilometro()
        elif opcao == 9:
            multa_porplaca()
        elif opcao == 10:
            multa_degeral()
        elif opcao == 11:
            print('Aplicacao finalizada...')
            break
        else:
            print('')
            print('\033[31mERRO NA APLICACAO, INSIRA OUTRO VALOR\033[m')
            print('')
