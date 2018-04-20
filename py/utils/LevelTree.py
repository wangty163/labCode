class LevelTree:
    class Node:
        def __init__(self, value=None):
            self.__parent = None
            self.__children = list()
            self.__id = -1
            self.__level = -1
            self.__value = value

        @property
        def parent(self):
            return self.__parent
        @property
        def children(self):
            return iter(self.__children)
        @property
        def id(self):
            return self.__id
        @property
        def level(self):
            return self.__level
        @property
        def value(self):
            return self.__value
        @property
        def pre(self):
            return self.parent.__children[self.id - 1]
        @property
        def next(self):
            return self.parent.children[self.id + 1]
        @property
        def first_child(self):
            return self.__children[0]

        def __iter__(self):
            self.__gen = self.__iter()
            return self
        def __next__(self):
            return next(self.__gen)

        def __iter(self):
            yield self
            for child in self.children:
                yield from child.__iter()

        def add_child(self, value):
            node = LevelTree.Node(value)
            node.__parent = self
            node.__id = len(self.__children)
            node.__level = self.level + 1
            self.__children.append(node)
            return node
        def add_next(self, value):
            assert self.__id + 1 == len(self.__parent.__children)
            return self.__parent.add_child(value)

    def __init__(self):
        self.root = LevelTree.Node()

    def build(self, lines):
        pre_level = -1
        node = self.root
        for level,line in lines:
            if level == pre_level:
                node = node.add_next(line)
            elif level > pre_level:
                assert level == pre_level + 1, line
                node = node.add_child(line)
            else:
                for i in range(pre_level - level):
                    node = node.parent
                node = node.add_next(line)
            pre_level = level