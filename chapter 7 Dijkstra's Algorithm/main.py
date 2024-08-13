# an undirected graph means that both nodes point to each other. That's a cycle
# Dijkstra's algorithm only works with directed acyclic graphs
# can’t use negative-weight edges with Dijkstra’s algorithm instead use Bellman-Ford algorithm

def find_lower_cost_node(costs, processed):

    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra_grokking():

    graph = {
        "start": {
            "a": 6,
            "b": 2
        },
        "a": {
            "fin": 1
        },
        "b": {
            "a": 3,
            "fin": 5
        },
        "fin": {}
    }

    costs = {
        "a": 6,
        "b": 2,
        "fin": float("inf")
    }

    parents = {
        "a": "start",
        "b": "start",
        "fin": None
    }

    processed = []

    node = find_lower_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lower_cost_node(costs, processed)

    print(costs)
    print(parents)


def main():

    dijkstra_grokking()

    return True


if __name__ == '__main__':
    main()
