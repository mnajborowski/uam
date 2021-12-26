import random


def pop_random_element(elements):
    return elements.pop(random.randrange(len(elements)))


class Tree:
    def __init__(self, n):
        self.n = n

    def generate(self):
        tree_nodes = []
        tree = []
        non_tree_nodes = list(range(1, self.n + 1))
        tree_nodes.append(pop_random_element(non_tree_nodes))
        for i in range(0, self.n - 1):
            random_tree_node = random.choice(tree_nodes)
            random_non_tree_node = pop_random_element(non_tree_nodes)
            tree.append([random_tree_node, random_non_tree_node])
            tree_nodes.append(random_non_tree_node)
        return tree
