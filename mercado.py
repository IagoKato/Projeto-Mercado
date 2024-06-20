from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_float_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('Bem vindo ao Shop')
    print('Selecione uma opção:')
    print('1 - Cadastrar produto')
    print('2 - Lista de produto')
    print('3 - Comprar produto')
    print('4 - Fechar pedido')
    print('5 - Ver carrinho')
    print('6 - Sair do shop')

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        fechar_pedido()
    elif opcao == 5:
        visualizar_carrinho()
    elif opcao == 6:
        print('Volte sempre')
        sleep(2)
    else:
        print('Opção invalída')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')

    nome: str = input('Nome do produto: ')
    preco: float = float(input('Preço do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'Produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Lista de produtos')
        print('-----------------')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Anda não possuem produtos cadastrados')
    sleep(2)
    menu()


def comprar_produtos() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        for produto in produtos:
            print('-----------------------')
            print(produto)
            print('-----------------------')
            sleep(1)
        codigo = int(input())

        produto: Produto = pegar_produto_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'Produto {produto.nome} agora possui {quantidade + 1} unidade no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                    if not tem_no_carrinho:
                        prod = {produto: 1}
                        carrinho.append(prod)
                        print(f'O produto {produto.nome} foi adicionado com sucesso!')
                        sleep(2)
                        menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado com sucesso!')
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos cadastrados')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos do carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('--------------')
                sleep(1)
    else:
        print('Ainda não tem produtos no carrinho')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-------------------------')
                sleep(1)
        print(f'Fatura é {formata_float_moeda(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não possue produtos no carrinho')
    sleep(2)
    menu()


def pegar_produto_codigo(codigo: int) -> Produto:
    product: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            product = produto
    return product


if __name__ == '__main__':
    main()
