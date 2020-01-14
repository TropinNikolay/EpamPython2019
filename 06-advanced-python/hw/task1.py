"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.length = len(self.graph)
        self.counter = 0
        self.bfs()

    def bfs(self):
        i = 0
        start = list(self.graph)[i]
        queue = [start]
        while queue:
            vertex = queue.pop(0)

            if vertex not in self.visited:
                self.visited.append(vertex)

            for ver in self.graph[vertex]:
                if ver not in self.visited:
                    queue.append(ver)

            if len(self.visited) != len(self.graph) and not queue:
                queue.append(list(self.graph)[i + 1])

        return self.visited

    def __next__(self):
        if self.counter < self.length:
            self.counter += 1
            return self.visited[self.counter - 1]
        else:
            self.counter = 0
            self.visited = []
            raise StopIteration

    def __iter__(self):
        self.counter = 0
        self.bfs()
        return self


E = {"A": ["B", "C", "D"], "B": ["C"], "C": [], "D": ["A"]}
A = {"B": ["C"], "A": ["B", "C", "D"], "C": [], "D": ["A"]}
C = {
    "A": ["B", "C", "D"],
    "C": ["E"],
    "B": ["G", "F"],
    "G": [],
    "F": [],
    "E": [],
    "D": [],
}

graph = Graph(E)
# graph = Graph(A)
# graph = Graph(C)

print(next(graph))
print(next(graph))
print(next(graph))
print(next(graph))

print("First loop")
for vertex in graph:
    print(vertex)

for vertex in graph:
    print("Second loop", vertex)
