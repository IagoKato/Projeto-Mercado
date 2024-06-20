Projeto Mercado Simples em Python

Este projeto Python simula um sistema básico de gerenciamento de um mercado, permitindo cadastrar produtos, listar produtos cadastrados, adicionar produtos ao carrinho de compras, visualizar o carrinho e fechar um pedido.
Estrutura do Projeto

    projeto-mercado/
    │
    ├── mercado.py
    │
    └── models/
    └── produto.py
    │
    └── utils/
        └── helper.py

Descrição do Projeto

O projeto consiste em um programa interativo de linha de comando que oferece as seguintes funcionalidades:

- Cadastro de Produto: Permite cadastrar um novo produto especificando nome e preço.

- Listagem de Produtos: Lista todos os produtos cadastrados até o momento.

- Compra de Produtos: Permite adicionar produtos ao carrinho de compras utilizando o código do produto.

- Visualização do Carrinho: Mostra os produtos atualmente no carrinho de compras, incluindo suas quantidades.

- Fechamento de Pedido: Calcula o valor total da compra com base nos produtos no carrinho e finaliza a compra, limpando o carrinho em seguida.

- Saída do Programa: Encerra a execução do programa.

Arquivos Principais

- mercado.py: Contém toda a lógica do programa principal, incluindo funções para interação com o usuário, manipulação do carrinho e chamadas às funcionalidades dos produtos.

- models/produto.py: Define a classe Produto que possui atributos como código, nome e preço. Também contém um método para formatar o preço em formato de moeda.

- utils/helper.py: Fornece uma função auxiliar formata_float_moeda para formatar valores float em moeda (duas casas decimais).

Como Executar

Para executar o programa, simplesmente execute o arquivo mercado.py. Ele inicializará o menu principal onde você pode escolher entre as opções disponíveis.

OBS: Em desenvolvimento. Criação de dashboard