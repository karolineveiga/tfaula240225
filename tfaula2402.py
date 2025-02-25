def adicionar_produto(inventario):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))

    if nome in inventario:
        inventario[nome]['quantidade'] += quantidade
        print(f"Produto '{nome}' já existente. Quantidade aumentada.")
    else:
        inventario[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado ao inventário.")

def remover_produto(inventario):
    nome = input("Digite o nome do produto a ser removido: ")
    
    if nome in inventario:
        del inventario[nome]
        print(f"Produto '{nome}' removido do inventário.")
    else:
        print(f"Produto '{nome}' não encontrado no inventário.")

def listar_produtos(inventario):
    if not inventario:
        print("Inventário vazio.")
    else:
        print("\nProdutos no inventário:")
        for nome, dados in inventario.items():
            print(f"Nome: {nome} | Preço: R${dados['preco']:.2f} | Quantidade: {dados['quantidade']}")

def menu():
    inventario = {}
    
    while True:
        print("\nMenu de Inventário")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto(inventario)
        elif opcao == '2':
            remover_produto(inventario)
        elif opcao == '3':
            listar_produtos(inventario)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
