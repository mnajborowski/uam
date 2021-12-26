import lab4.flow_network
import lab4.graph


def __read_network_from_file(path):
    max_node = 0
    network = []
    network_strings = open(path, "r").read().splitlines()
    for edge in network_strings:
        edge_elements = [int(element) for element in edge.split(" ")]
        local_max_node = max(edge_elements)
        if local_max_node > max_node:
            max_node = local_max_node
        network.append([[edge_elements[0], edge_elements[1]], edge_elements[2]])
    return max_node, network


def print_max_edge_disjoint_paths_for_network_from_file(path):
    max_node, network = __read_network_from_file(path)
    modified_network = [[edge, 1] for [edge, _] in network]
    lab4.flow_network.FlowNetwork(max_node, modified_network).print_max_flow()


if __name__ == '__main__':
    print_max_edge_disjoint_paths_for_network_from_file("../lab4/flow_network.txt")
