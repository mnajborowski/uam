from pip._vendor.msgpack.fallback import xrange

from lab4.graph import Graph
import random
import math


class FlowNetwork:
    def __init__(self, n, network=None):
        self.n = n
        if network is not None:
            self.__network = network
        else:
            self.__network = self.__generate()
        self.__capacity_matrix = self.__generate_capacity_matrix()
        self.__max_flow = self.__max_flow()

    def __generate(self):
        m = random.randint(math.ceil(self.n / 2), self.n - 1)
        max_threshold = random.randint(math.ceil(self.n / 2), self.n - 1)
        graph = Graph(self.n, m).generate_complete_graph()
        return [[edge, random.randint(1, max_threshold)] for edge in graph]

    def __generate_capacity_matrix(self):
        capacity_matrix = [[0] * self.n for _ in range(self.n)]
        for outgoing in range(self.n):
            for ingoing in range(self.n):
                capacity = next(
                    (threshold for [edge, threshold] in self.__network if edge == [outgoing + 1, ingoing + 1]), 0)
                capacity_matrix[outgoing][ingoing] = capacity
        return capacity_matrix

    def __bfs(self, F):
        s = 0
        t = self.n - 1
        queue = [s]
        paths = {s: []}
        if s == t:
            return paths[s]
        while queue:
            u = queue.pop(0)
            for v in xrange(len(self.__capacity_matrix)):
                if (self.__capacity_matrix[u][v] - F[u][v] > 0) and v not in paths:
                    paths[v] = paths[u] + [(u, v)]
                    if v == t:
                        return paths[v]
                    queue.append(v)
        return None

    def __max_flow(self):
        n = len(self.__capacity_matrix)
        F = [[0] * n for _ in xrange(n)]
        path = self.__bfs(F)
        while path is not None:
            flow = min(self.__capacity_matrix[u][v] - F[u][v] for u, v in path)
            for u, v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = self.__bfs(F)
        return sum(F[0][i] for i in xrange(n))

    def write_network_to_file(self, path):
        f = open(path, "w")
        for edge in self.__network:
            f.write("{} {} {}\n".format(edge[0][0], edge[0][1], edge[1]))
        f.close()

    def print_network(self):
        print(self.__network)

    def print_capacity_matrix(self):
        for row in self.__capacity_matrix:
            print(row)

    def print_max_flow(self):
        print(self.__max_flow)


def read_network_from_file(path):
    max_node = 0
    network = []
    network_strings = open(path, "r").read().splitlines()
    for edge in network_strings:
        edge_elements = [int(element) for element in edge.split(" ")]
        local_max_node = max(edge_elements)
        if local_max_node > max_node:
            max_node = local_max_node
        network.append([[edge_elements[0], edge_elements[1]], edge_elements[2]])
    return FlowNetwork(max_node, network)


if __name__ == '__main__':
    FlowNetwork(10).write_network_to_file("flow_network.txt")
    flow_network = read_network_from_file("flow_network.txt")
    flow_network.print_network()
    flow_network.print_capacity_matrix()
    flow_network.print_max_flow()
