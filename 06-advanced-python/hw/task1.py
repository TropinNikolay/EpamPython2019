"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, E):
        self.E = E
        self.visited = list()
        self.length = len(self.E)
        self.counter = 0

    def bfs(self):
        start = list(self.E.keys())[0]
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in self.visited:
                self.visited.append(vertex)
                tmp = []
                for ver in self.E[vertex]:
                    if ver not in self.visited:
                        tmp.append(ver)
                queue.extend(tmp)
        return self.visited

    def __next__(self):
        if self.counter < self.length:
            self.counter += 1
            self.bfs()
            return self.visited[self.counter - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
