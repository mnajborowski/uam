from lab4.tree import Tree
import random


class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def generate(self):
        graph = Tree(self.n).generate()
        edges = [[i, j] for i in range(1, self.n + 1) for j in range(1, self.n + 1) if i != j and [i, j] not in graph]
        for _ in range(0, self.m - self.n + 1):
            random_edge = random.choice(edges)
            graph.append(random_edge)
            edges.remove(random_edge)
        graph.sort()
        return graph

    def generate_complete_graph(self):
        graph = Tree(self.n).generate()
        for index, edge in list(enumerate(graph)):
            if edge[1] == 1 or edge[0] == self.n:
                graph[index] = [edge[1], edge[0]]
        # graph = list(set(graph))
        all_edges = [[outgoing, ingoing] for outgoing in range(1, self.n + 1) for ingoing in range(1, self.n + 1) if
                     outgoing != ingoing and [outgoing, ingoing] not in graph and ingoing != 1 and outgoing != self.n]
        for _ in range(0, self.m - self.n + 1):
            random_edge = random.choice(all_edges)
            graph.append(random_edge)
            all_edges.remove(random_edge)

        source_outgoing_edges = [edge for edge in graph if edge[0] == 1]
        if len(source_outgoing_edges) == 0:
            source_outgoing_edge = random.choice([edge for edge in all_edges if edge[0] == 1])
            graph.append(source_outgoing_edge)
            all_edges.remove(source_outgoing_edge)

        target_ingoing_edges = [edge for edge in graph if edge[1] == self.n]
        if len(target_ingoing_edges) == 0:
            target_ingoing_edge = random.choice([edge for edge in all_edges if edge[1] == self.n])
            graph.append(target_ingoing_edge)
            all_edges.remove(target_ingoing_edge)

        for node in range(2, self.n):
            current_outgoing_edges = [edge for edge in graph if edge[0] == node]
            if len(current_outgoing_edges) == 0:
                missing_outgoing_edge = random.choice([[outgoing, ingoing] for [outgoing, ingoing] in all_edges if
                                                       outgoing == node and [ingoing, outgoing] not in graph])
                graph.append(missing_outgoing_edge)
                all_edges.remove(missing_outgoing_edge)

            current_ingoing_edges = [edge for edge in graph if edge[1] == node]
            if len(current_ingoing_edges) == 0:
                missing_ingoing_edge = random.choice([[outgoing, ingoing] for [outgoing, ingoing] in all_edges if
                                                      ingoing == node and [ingoing, outgoing] not in graph])
                graph.append(missing_ingoing_edge)
                all_edges.remove(missing_ingoing_edge)
        graph.sort()
        return graph