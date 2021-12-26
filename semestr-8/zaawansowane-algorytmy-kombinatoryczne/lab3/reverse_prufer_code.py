class ReversePruferCode:
    def __init__(self, n, code):
        self.n = n
        self.code = code

    def print(self):
        L1 = [int(v) for v in self.code.split()]
        L1_copy = [int(v) for v in self.code.split()]
        L2 = list(range(1, n + 1))
        nodes = set(range(1, n))
        tree = []
        for k in range(0, n - 2):
            diff = list(set(L2) - set(L1))
            lowest_helper_element = min(diff)
            code_element = L1_copy[k]
            tree.append(sorted([code_element, lowest_helper_element]))
            L1.pop(0)
            L2 = list(filter(lowest_helper_element.__ne__, L2))
        tree.append(sorted([L2[0], L2[1]]))
        sorted_tree = list(sorted(tree, key=lambda l: (l[0], l[1])))
        for edge in sorted_tree:
            print(*edge, sep=" ")


if __name__ == '__main__':
    n = int(input())
    code = input()
    assert (3 <= n <= 100)
    assert (len(code.split()) == n - 2)
    ReversePruferCode(n, code).print()
