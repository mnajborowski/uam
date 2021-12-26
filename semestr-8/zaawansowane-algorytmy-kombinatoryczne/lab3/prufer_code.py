import itertools


class PruferCode:
    def __init__(self, n, tree):
        self.n = n
        self.tree = tree

    def __get_lowest_node_tag_by_range(self):
        flat_tree = list(itertools.chain.from_iterable(self.tree))
        distinct_nodes = set(flat_tree)
        node_ranges = []
        for node in distinct_nodes:
            node_ranges.append([node, flat_tree.count(node)])
        sorted_node_ranges = list(sorted(node_ranges, key=lambda l: (l[1], l[0])))
        return sorted_node_ranges[0][0]

    def __get_edge_to_remove(self):
        lowest_node_tag_by_range = self.__get_lowest_node_tag_by_range()
        edge_to_remove = next(filter(lambda edge: edge[1] == lowest_node_tag_by_range, self.tree), None)
        if edge_to_remove is None:
            return next(filter(lambda edge: edge[0] == lowest_node_tag_by_range, self.tree)), 1
        else:
            return edge_to_remove, 0

    def print(self):
        code = []
        while len(self.tree) > 1:
            edge_to_remove, code_node_index = self.__get_edge_to_remove()
            code.append(edge_to_remove[code_node_index])
            self.tree = list(filter(edge_to_remove.__ne__, self.tree))
        print(*code, sep=" ")


if __name__ == '__main__':
    n = int(input())
    tree = []
    for i in range(0, n - 1):
        tree.append([int(node) for node in input().split()])
    assert (3 <= n <= 100)
    assert (len(tree) == n - 1)
    PruferCode(n, tree).print()
