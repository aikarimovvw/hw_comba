class Node:
    def __init__(self, key):
        """
        Инициализация узла дерева поиска.
        :param key: Значение, хранимое в узле.
        """
        self.key = key        # Значение узла
        self.left = None      # Левый потомок
        self.right = None     # Правый потомок
        self.parent = None    # Родитель (опционально)

    def __repr__(self):
        return f"Node({self.key})"

class BinarySearchTree:
    def __init__(self):
        """
        Инициализация пустого дерева поиска.
        """
        self.root = None

    def insert(self, key):
        """
        Вставка нового ключа в дерево.
        :param key: Значение для вставки.
        """
        new_node = Node(key)
        y = None
        x = self.root

        # Поиск места для вставки нового узла
        while x is not None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y is None:
            # Дерево было пустым
            self.root = new_node
            print(f"Вставлен корневой узел: {new_node.key}")
        elif new_node.key < y.key:
            y.left = new_node
            print(f"Вставлен узел {new_node.key} как левый потомок {y.key}")
        else:
            y.right = new_node
            print(f"Вставлен узел {new_node.key} как правый потомок {y.key}")

    def search(self, key):
        """
        Поиск узла с заданным ключом.
        :param key: Значение для поиска.
        :return: Узел, если найден, иначе None.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or key == node.key:
            if node:
                print(f"Найден узел: {node.key}")
            else:
                print(f"Узел с ключом {key} не найден.")
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def minimum(self, node=None):
        """
        Поиск узла с минимальным ключом в поддереве.
        :param node: Корень поддерева. Если None, используется корень дерева.
        :return: Узел с минимальным ключом.
        """
        if node is None:
            node = self.root
        current = node
        while current.left is not None:
            current = current.left
        print(f"Минимальный ключ в поддереве: {current.key}")
        return current

    def maximum(self, node=None):
        """
        Поиск узла с максимальным ключом в поддереве.
        :param node: Корень поддерева. Если None, используется корень дерева.
        :return: Узел с максимальным ключом.
        """
        if node is None:
            node = self.root
        current = node
        while current.right is not None:
            current = current.right
        print(f"Максимальный ключ в поддереве: {current.key}")
        return current

    def successor(self, node):
        """
        Поиск преемника (следующего по возрастанию) для данного узла.
        :param node: Узел, для которого ищется преемник.
        :return: Преемник узла или None, если его нет.
        """
        if node.right is not None:
            return self.minimum(node.right)
        y = node.parent
        while y is not None and node == y.right:
            node = y
            y = y.parent
        if y:
            print(f"Преемник узла {node.key} это {y.key}")
        else:
            print(f"У узла {node.key} нет преемника.")
        return y

    def predecessor(self, node):
        """
        Поиск предшественника (предыдущего по убыванию) для данного узла.
        :param node: Узел, для которого ищется предшественник.
        :return: Предшественник узла или None, если его нет.
        """
        if node.left is not None:
            return self.maximum(node.left)
        y = node.parent
        while y is not None and node == y.left:
            node = y
            y = y.parent
        if y:
            print(f"Предшественник узла {node.key} это {y.key}")
        else:
            print(f"У узла {node.key} нет предшественника.")
        return y

    def transplant(self, u, v):
        """
        Замена поддерева, корнем которого является узел u, на поддерево с корнем v.
        :param u: Узел, который будет заменен.
        :param v: Узел, который заменит узел u.
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, key):
        """
        Удаление узла с заданным ключом из дерева.
        :param key: Значение для удаления.
        """
        node = self.search(key)
        if node is None:
            print(f"Узел с ключом {key} не найден. Удаление невозможно.")
            return

        print(f"Удаление узла: {node.key}")

        if node.left is None:
            self.transplant(node, node.right)
            if node.right:
                print(f"Замена узла {node.key} его правым потомком {node.right.key}")
            else:
                print(f"Замена узла {node.key} отсутствующим правым потомком")
        elif node.right is None:
            self.transplant(node, node.left)
            if node.left:
                print(f"Замена узла {node.key} его левым потомком {node.left.key}")
            else:
                print(f"Замена узла {node.key} отсутствующим левым потомком")
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
                print(f"Замена узла {y.key} его правым потомком {y.right.key}")
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            print(f"Замена узла {node.key} узлом {y.key}")

    def inorder_traversal(self, node=None, visit=lambda x: print(x.key)):
        """
        Обход дерева в симметричном порядке (in-order).
        :param node: Текущий узел для обхода. Если None, начинается с корня.
        :param visit: Функция для обработки узла.
        """
        if node is None:
            node = self.root
        if node is not None:
            self.inorder_traversal(node.left, visit)
            visit(node)
            self.inorder_traversal(node.right, visit)

    def preorder_traversal(self, node=None, visit=lambda x: print(x.key)):
        """
        Прямой обход дерева (pre-order).
        :param node: Текущий узел для обхода. Если None, начинается с корня.
        :param visit: Функция для обработки узла.
        """
        if node is None:
            node = self.root
        if node is not None:
            visit(node)
            self.preorder_traversal(node.left, visit)
            self.preorder_traversal(node.right, visit)

    def postorder_traversal(self, node=None, visit=lambda x: print(x.key)):
        """
        Обратный обход дерева (post-order).
        :param node: Текущий узел для обхода. Если None, начинается с корня.
        :param visit: Функция для обработки узла.
        """
        if node is None:
            node = self.root
        if node is not None:
            self.postorder_traversal(node.left, visit)
            self.postorder_traversal(node.right, visit)
            visit(node)


def main():
    bst = BinarySearchTree()

    # Вставка элементов
    elements = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
    print("Вставка элементов:")
    for el in elements:
        bst.insert(el)
    print("\nОбход дерева в порядке возрастания (in-order):")
    bst.inorder_traversal()

    # Поиск элементов
    print("\nПоиск элементов:")
    bst.search(7)
    bst.search(10)

    # Поиск минимума и максимума
    print("\nПоиск минимума и максимума:")
    bst.minimum()
    bst.maximum()

    # Поиск преемника и предшественника
    print("\nПреемник и предшественник узла 15:")
    node_15 = bst.search(15)
    if node_15:
        bst.successor(node_15)
        bst.predecessor(node_15)

    # Удаление элементов
    print("\nУдаление элементов:")
    bst.delete(6)
    print("\nОбход дерева после удаления 6 (in-order):")
    bst.inorder_traversal()

    bst.delete(15)
    print("\nОбход дерева после удаления 15 (in-order):")
    bst.inorder_traversal()

    # Дополнительные обходы
    print("\nПрямой обход дерева (pre-order):")
    bst.preorder_traversal()

    print("\nОбратный обход дерева (post-order):")
    bst.postorder_traversal()

if __name__ == "__main__":
    main()
