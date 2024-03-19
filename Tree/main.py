class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None): # Инициализация
        self.root = root
        pass

    def __str__(self): # Вывод дерева
        pass

    def __len__(self): # Вывод длины дерева
        pass

    def search(self): # Поиск элемента в дереве
        pass

    def add(self): # Добавление элемента в дерево
        pass

    def remove(self): # Удаление элемента из дерева
        pass

    def balancing(self): # Балансировка
        pass

    def bfs(self):
        '''Обход дерева в ширину'''
        pass

    def dfs(self):
        '''Обход дерева в глубину'''
        pass