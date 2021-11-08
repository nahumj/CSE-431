import collections
import pprint


class Node:
    def __init__(self, id_, data=None):
        self.id_ = id_
        self.data = data

    def __eq__(self, other):
        return self.id_ == other.id_

    def __hash__(self):
        return hash(self.id_)

    def __repr__(self):
        return f"Node(id_={self.id_}, data={self.data})"


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = collections.defaultdict(list)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, start_node_id, end_node_id, data=None):
        assert Node(start_node_id) in self.nodes
        assert Node(end_node_id) in self.nodes
        self.edges[start_node_id].append((end_node_id, data))

    def __repr__(self):
        return f"Graph(nodes={pprint.pformat(self.nodes)}, edges={pprint.pformat(self.edges)})"

    def breadth_first_traversal(self, start_id):
        discovered = collections.deque()
        fully_explored = []

        discovered.append(start_id)

        while discovered:
            node_id = discovered.popleft()
            for child_id, data in self.edges[node_id]:
                if child_id not in discovered and not child_id in fully_explored:
                    discovered.append(child_id)
            fully_explored.append(node_id)

        return fully_explored

    def depth_first_traversal(self, start_id):
        discovered = []
        fully_explored = []

        discovered.append(start_id)

        while discovered:
            node_id = discovered[-1]
            for child_id, data in self.edges[node_id]:
                if child_id not in discovered and not child_id in fully_explored:
                    discovered.append(child_id)
                    break
            else:
                # nothing added to discovered
                discovered.pop()
                fully_explored.append(node_id)

        return fully_explored


def main():
    letter_nodes = "ABCDEFGHIJKL"
    list_of_tuple_edges = [
        ("A", "B"), ("A", "C"),
        ("B", "C"), ("B", "F"),
        ("C", "D"), ("C", "E"),
        ("D", "G"),
        ("E", "F"), ("E", "G"),
        ("F", "H"), ("F", "I"),
        ("G", "H"),
        ("H", "I"),
        ("I", "J"), ("I", "L"),
        ("J", "K"), ("J", "L"),
    ]
    graph = Graph()
    for letter in letter_nodes:
        graph.add_node(Node(letter))
    for left_id, right_id in list_of_tuple_edges:
        graph.add_edge(left_id, right_id)
        graph.add_edge(right_id, left_id)

    print(graph)

    print(graph.breadth_first_traversal("A"))
    print(graph.depth_first_traversal("A"))


if __name__ == "__main__":
    main()
