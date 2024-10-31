# criação do crud utilizando o mongo
from model.produto import Produto
from service.mongo_handler import MongoHandler

db_handler = MongoHandler()

def mostrar_produtos():
    produtos = db_handler.get_produtos()
    for produto in produtos:
        print(f"{produto['nome']} - {produto['preco']:.2f}")

def inserir_produto(p_nome, p_preco):
    produto = Produto(p_nome, p_preco)
    db_handler.insert_produto(produto)

def atualizar_produto(nome_atual, novo_nome, novo_preco):
    filtro = {"nome": nome_atual}
    novos_valores = {"nome": novo_nome, "preco": novo_preco}
    resultado = db_handler.update_produto(filtro, novos_valores)
    if resultado > 0:
        print("Produto atualizado com sucesso")
    else:
        print("Produto não encontrado")

def deletar_produto(nome):
    filtro = {"nome": nome}
    resultado = db_handler.delete_produto(filtro)
    if resultado > 0:
        print("Produto excluído com sucesso")
    else:
        print("Produto não encontrado")


def mostrar_menu():
    while True:
        print("""
            Menu de opções. Escolha sua opção:
            1 - Inserir produto
            2 - Listar produtos
            3 - Atualizar produto
            4 - Excluir produto
            0 - Sair
        """)

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            print("Informe os dados do produto:")
            nome = input("Nome: ")
            try:
                preco = float(input("Preço: "))
                inserir_produto(nome, preco)
                print("Produto inserido com sucesso.")
            except ValueError:
                print("Erro: o preço deve ser um número.")
            mostrar_produtos()
        elif opcao == 2:
            mostrar_produtos()
        elif opcao == 3:
            # Atualizar produto
            nome_atual = input("Nome do produto a atualizar: ")
            novo_nome = input("Novo nome: ")
            try:
                novo_preco = float(input("Novo preço: "))
                atualizar_produto(nome_atual, novo_nome, novo_preco)
            except ValueError:
                print("Erro: o preço deve ser um número.")

        elif opcao == 4:
            # Excluir produto
            nome = input("Nome do produto a excluir: ")
            deletar_produto(nome)

        elif opcao == 0:
            print("Você optou por sair do programa.")
            break  # Encerra o loop e sai do programa

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    mostrar_menu()