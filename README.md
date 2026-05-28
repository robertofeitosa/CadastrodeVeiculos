# Cadastro de Veiculos

Projeto simples desenvolvido em Python para gerenciar cadastros de veiculos pelo terminal.

O sistema permite cadastrar, listar, pesquisar, modificar e excluir veiculos. Tambem possui funcionalidades para registrar multas e consultar as multas de um veiculo especifico pela placa ou visualizar as multas de todos os veiculos cadastrados.

## Funcionalidades

- Cadastrar veiculos
- Listar todos os veiculos cadastrados
- Pesquisar veiculo por placa
- Pesquisar veiculos por UF
- Pesquisar veiculos por ano
- Pesquisar veiculos por quilometragem
- Modificar dados de um veiculo cadastrado
- Excluir veiculo por placa
- Adicionar multas aos veiculos
- Consultar multas por placa
- Listar multas de todos os veiculos

## Como executar

Para rodar o projeto, tenha o Python instalado no computador.

No terminal, acesse a pasta do projeto e execute:

```bash
python main.py
```

Depois disso, o menu principal sera exibido no terminal.

## Estrutura do projeto

```text
CadastrodeVeiculos/
|-- main.py
`-- sistema/
    |-- adicionarmultaoveiculo.py
    |-- cadastrarveiculo.py
    |-- excluirporplaca.py
    |-- listarveiculos.py
    |-- menu.py
    |-- modificarveiculo.py
    |-- multadetodos.py
    |-- pesquisaplaca.py
    |-- procurarmultasporplaca.py
    |-- veiculoporano.py
    |-- veiculoporkm.py
    `-- veiculosporuf.py
```

## Observacoes

Os dados sao armazenados em listas durante a execucao do programa. Isso significa que, ao fechar o sistema, os cadastros nao ficam salvos permanentemente.

Este projeto foi criado com objetivo de praticar conceitos iniciais de Python, como listas, funcoes, condicionais, repeticoes, modularizacao e manipulacao de dados pelo terminal.
