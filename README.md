# CRUD-Python-MongoDB
Este é um projeto de exemplo que implementa um sistema CRUD (Create, Read, Update, Delete) utilizando Python e MongoDB. Ele permite gerenciar produtos com informações de nome e preço, armazenadas em um banco de dados MongoDB.

## Estrutura do Projeto

- ``main.py``: Arquivo principal que inicia o programa e exibe o menu de opções para o usuário.
- ``model/produto.py``: Define a classe Produto, que representa o modelo de dados dos produtos.
- ``service/mongo_handler.py``: Contém funções para conexão e manipulação do banco de dados MongoDB.

## Funcionalidades

O programa permite:

1. **Criar** um novo produto.
2. **Listar** todos os produtos
3. **Atualizar** um produto existente
4. **Excluir** um produto

## **Requisitos**

- **Python 3.x** instalado
- **MongoDB** configurado e em execução

## **Instalação**

1. Clone o repositório:

    ``` bash 
    git clone https://github.com/felipezzz1/CRUD-Python-MongoDB.git
    ```

2. Instale as dependências necessárias

3. Configure o arquivo ``.env`` com as informações de conexão com o MongoDB.

## **Uso**

Para iniciar o programa, execute o arquivo ``main.py``:

## **Estrutura do Menu**

O menu oferece as seguintes opções:

- Adicionar novo produto
- Listar todos os produtos
- Atualizar um produto
- Excluir um produto
- Sair do programa