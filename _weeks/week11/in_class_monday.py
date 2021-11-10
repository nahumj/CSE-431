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
        return f"Node(id_ = {self.id_}, data = {self.data})"

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = collections.defaultdict(list)

    def add_node(self, node):
        assert node not in self.nodes
        assert isinstance(node, Node)
        self.nodes.append(node)
    
    def add_edge(self, start_node_id, end_node_id, data=None):
        assert end_node_id not in self.edges[start_node_id]
        self.edges[start_node_id].append((end_node_id, data))

    def __repr__(self):
        return f"Graph(nodes={pprint.pformat(self.nodes)}, edges={pprint.pformat(self.edges)})"
    
    def breadth_first_traversal(self, start_node_id):
        discovered = collections.deque()
        fully_explored = []
        done_with = set()

        discovered.append(start_node_id)
        done_with.add(start_node_id)

        while discovered:
            node_id = discovered.popleft()
            for child_node_id, _ in self.edges[node_id]:
                if child_node_id not in done_with:
                    discovered.append(child_node_id)
                    done_with.add(child_node_id)
            fully_explored.append(node_id)

        return fully_explored
    

    def depth_first_traversal(self, start_node_id):
        discovered = []
        fully_explored = []
        done_with = set()

        discovered.append(start_node_id)
        done_with.add(start_node_id)

        while discovered:
            node_id = discovered[-1]
            for child_node_id, _ in self.edges[node_id]:
                if child_node_id not in done_with:
                    discovered.append(child_node_id)
                    done_with.add(child_node_id)
                    break
            else:
                pop_id = discovered.pop()
                assert pop_id == node_id
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

    for letter_id in letter_nodes:
        node = Node(letter_id)
        graph.add_node(node)

    for start_node, end_node in list_of_tuple_edges:
        graph.add_edge(start_node, end_node)
        graph.add_edge(end_node, start_node)
    print(graph)
    print(graph.depth_first_traversal("A"))


if __name__ == "__main__":
    main()