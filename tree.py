# Classe para armazenar os dados.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # Função para retornar o objeto Node em forma de string.

    def __str__(self):
        return str(self.data)

# classe que vai estruturar a árvore a partir da raiz.


class BinaryTree:
    def __init__(self, data):
        node = Node(data)
        self.root = node


# programa principal para inserção e exibição dos dados.
if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print('Raiz', end=' ')
    print(tree.root)
    print('Filho esquerdo', end=' ')
    print(tree.root.left)
    print('Filho dirteito', end=' ')
    print(tree.root.right)
