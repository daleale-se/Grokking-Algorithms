from collections import deque
from bfs import bfs


def person_is_seller(name):
    return name[0] == "p"


def bfs_grokking():

    # directed graph
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }

    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def main():

    # (node) : (n of edges)
    graph = {
        "A": ["B", "C"],
        "B": ["J", "D"],
        "C": ["D", "F"],
        "D": ["E"],
        "E": [],
        "F": ["G", "M"],
        "G": ["A", "I", "H"],
        "H": [],
        "I": ["K"],
        "J": ["L"],
        "K": ["P", "L"],
        "L": ["O"],
        "M": ["N"],
        "N": [],
        "O": [],
        "P": []
    }

    bfs(graph, "A")

    return True


main()
