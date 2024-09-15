# an undirected graph means that both nodes point to each other. That's a cycle
# Dijkstra's algorithm only works with directed acyclic graphs
# can’t use negative-weight edges with Dijkstra’s algorithm instead use Bellman-Ford algorithm

from dijkstra_grokking import dijkstra_grokking


def main():

    dijkstra_grokking()


if __name__ == '__main__':
    main()
