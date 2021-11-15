import collections
import pprint
import copy

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
        self.nodes = {}
        self.edges = collections.defaultdict(list)

    def add_node(self, node):
        assert isinstance(node, Node)
        self.nodes[node.id_] = node
    
    def remove_node(self, node):
        # remove node as start of edge
        del self.edges[node.id_]

        #remove node as end of edge
        for start_id, end_list in self.edges.items():
            new_end_list = [(end_id, data) for end_id, data in end_list if end_id != node.id_]
            self.edges[start_id] = new_end_list


        del self.nodes[node.id_]
    
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
    
    def has_edge(self, start_id, end_id):
        for existing_end_id, _ in self.edges[start_id]:
            if existing_end_id == end_id:
                return True
        return False
    
    def mst_prims_algorithm(self, start_node=None):
        mst = Graph()
        if start_node is None:
            start_node = next(iter(self.nodes.values()))
        node = start_node
        mst.add_node(node)

        edges_to_consider = []
        while len(mst.nodes) < len(self.nodes):
            for end_id, weight in self.edges[node.id_]:
                edges_to_consider.append((weight, node.id_, end_id))
            edges_to_consider.sort()
            while True:
                minimum_weight, start_id, end_id = edges_to_consider.pop(0)
                if end_id not in mst.nodes:
                    break
            mst.add_node(self.nodes[end_id])
            mst.add_edge(start_id, end_id, minimum_weight)
            node = self.nodes[end_id]

        return mst


def main():
    letter_nodes = "01234"
    list_of_tuple_edges_weights = [
        ("0", "1", 4), 
        ("0", "2", 4), 
        ("0", "3", 6),
        ("0", "4", 6), 
        ("1", "2", 2), 
        ("2", "3", 8), 
        ("3", "4", 9),
    ]
    graph = Graph()

    for letter_id in letter_nodes:
        node = Node(letter_id)
        graph.add_node(node)

    for start_node, end_node, weight in list_of_tuple_edges_weights:
        graph.add_edge(start_node, end_node, weight)
        graph.add_edge(end_node, start_node, weight)
    
    print(graph)
    print(graph.mst_prims_algorithm())



if __name__ == "__main__":
    main()