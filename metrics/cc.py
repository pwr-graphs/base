from itertools import product

from pylog import *


def clcc(net, node, threshold=1):
    """ Description
    # TODO
    :type net:
    :param net:

    :type node:
    :param node:

    :type threshold:
    :param threshold:

    :raises:

    :rtype:
    """
    lcc_sum = 0.0
    neighbors_counts = {}

    assert node in net.available_nodes()

    for layer in net.nx_layers:
        if node in layer.nodes():
            for neighbor in layer.neighbors(node):
                neighbors_counts[neighbor] = neighbors_counts.get(neighbor, 0) + 1

    neighbors_counts = {neighbor: occurrences for neighbor, occurrences
                        in neighbors_counts.items() if occurrences >= threshold}

    if not neighbors_counts:
        return lcc_sum

    for layer in net.layers_names:
        neighbors = neighbors_counts.keys()
        for v, h in product(neighbors, neighbors):
            lcc_sum += (net.has_edge(layer, h, v) + net.has_edge(layer, v, h))

    return lcc_sum / (2 * len(neighbors_counts) * len(net.nx_layers))
