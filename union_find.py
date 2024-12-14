class UnionFind:
    def __init__(self, size):
        """
        Инициализация структуры данных.
        :param size: Количество элементов.
        """
        self.parent = [i for i in range(size)]  # Каждый элемент является своим собственным родителем
        self.rank = [0] * size  # Ранг каждого элемента

    def find(self, x):
        """
        Найти корень множества, которому принадлежит элемент x.
        Применяется сжатие путей для оптимизации.
        :param x: Элемент для поиска.
        :return: Корень множества.
        """
        if self.parent[x] != x:
            print(f"Сжатие пути: элемент {x} имеет родителя {self.parent[x]}, рекурсивный вызов find({self.parent[x]})")
            self.parent[x] = self.find(self.parent[x])  # Рекурсивный вызов для поиска корня
        else:
            print(f"Элемент {x} является корнем.")
        return self.parent[x]

    def union(self, x, y):
        """
        Объединить множества, содержащие элементы x и y.
        Применяется объединение по рангу.
        :param x: Первый элемент.
        :param y: Второй элемент.
        :return: None
        """
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            print(f"Элементы {x} и {y} уже находятся в одном множестве.")
            return  # Они уже в одном множестве

        # Объединение по рангу
        if self.rank[x_root] < self.rank[y_root]:
            print(f"Ранг корня {x_root} меньше ранга корня {y_root}. Присоединяем {x_root} к {y_root}.")
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            print(f"Ранг корня {y_root} меньше ранга корня {x_root}. Присоединяем {y_root} к {x_root}.")
            self.parent[y_root] = x_root
        else:
            print(f"Ранги корней {x_root} и {y_root} равны. Присоединяем {y_root} к {x_root} и увеличиваем ранг {x_root}.")
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def connected(self, x, y):
        """
        Проверить, принадлежат ли элементы x и y одному множеству.
        :param x: Первый элемент.
        :param y: Второй элемент.
        :return: True, если элементы связаны, иначе False.
        """
        return self.find(x) == self.find(y)

    def print_sets(self):
        """
        Вывести текущее состояние множеств.
        """
        sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root in sets:
                sets[root].append(i)
            else:
                sets[root] = [i]
        for root, members in sets.items():
            print(f"Множество {root}: {members}")

def main():
    # Инициализация с 10 элементами (0-9)
    uf = UnionFind(10)

    # Объединяем некоторые множества
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(5, 6)
    uf.union(7, 8)
    uf.union(8, 9)

    print("\nТекущее состояние множеств после объединений:")
    uf.print_sets()

    # Проверяем связь между элементами
    print("\nПроверка связности:")
    print(f"0 и 2 связаны? {uf.connected(0, 2)}")  # True
    print(f"0 и 3 связаны? {uf.connected(0, 3)}")  # False
    print(f"7 и 9 связаны? {uf.connected(7, 9)}")  # True

    # Дополнительные объединения
    uf.union(2, 3)
    uf.union(5, 9)

    print("\nТекущее состояние множеств после дополнительных объединений:")
    uf.print_sets()

    # Повторная проверка связности
    print("\nПовторная проверка связности:")
    print(f"0 и 4 связаны? {uf.connected(0, 4)}")  # True
    print(f"5 и 8 связаны? {uf.connected(5, 8)}")  # True
    print(f"6 и 7 связаны? {uf.connected(6, 7)}")  # True

if __name__ == "__main__":
    main()
