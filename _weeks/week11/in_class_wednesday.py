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
        self.nodes = []
        self.edges = collections.defaultdict(list)

    def add_node(self, node):
        assert node not in self.nodes
        assert isinstance(node, Node)
        self.nodes.append(node)
    
    def remove_node(self, node):
        # remove node as start of edge
        del self.edges[node.id_]

        #remove node as end of edge
        for start_id, end_list in self.edges.items():
            new_end_list = [(end_id, data) for end_id, data in end_list if end_id != node.id_]
            self.edges[start_id] = new_end_list


        self.nodes.remove(node)
    
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

    def depth_first_traversal_tree(self, start_node_id):

        def decorate_tree(dft_tree, node_id, depth=0):
            # node's depth, is_leaf, children, back_edges
            children = [child_ids for child_ids, data in dft_tree.edges[node_id] if data is None]
            back_edges = [child_ids for child_ids, data in dft_tree.edges[node_id] if data is not None and data["back_edge"]]
            is_leaf = not children

            index = dft_tree.nodes.index(Node(node_id))
            dft_tree.nodes[index].data = {"depth": depth, "is_leaf": is_leaf, "children": children, "back_edges": back_edges}

            for child_id in children:
                decorate_tree(dft_tree, child_id, depth + 1)





        dft_tree = Graph()
        dft_tree.add_node(Node(start_node_id))
        
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
                    dft_tree.add_node(Node(child_node_id))
                    dft_tree.add_edge(node_id, child_node_id)
                    break
                elif (child_node_id in discovered and 
                        not dft_tree.has_edge(node_id, child_node_id) and 
                        not dft_tree.has_edge(child_node_id, node_id)):
                    dft_tree.add_edge(node_id, child_node_id, data={"back_edge": True})
            else:
                pop_id = discovered.pop()
                assert pop_id == node_id
                fully_explored.append(node_id)

        decorate_tree(dft_tree, start_node_id)
        return dft_tree

    def articulation_nodes_fast(self):
        dft_tree = self.depth_first_traversal_tree(self.nodes[0].id_)
        articulation_nodes = []
        for node in dft_tree.nodes:
            if node.data["depth"] == 0:
                #root
                if len(node.data["children"]) > 1:
                    articulation_nodes.append(node)
                    continue
            if node.data["is_leaf"]:
                continue
            #hard case
            for child_id in node.data["children"]:
                index = dft_tree.nodes.index(Node(child_id))
                child_node = dft_tree.nodes[index]
                is_safe_child = False
                for back_edge in child_node.data["back_edges"]:
                    back_edge_index = dft_tree.nodes.index(Node(back_edge))
                    back_edge_node = dft_tree.nodes[back_edge_index]
                    if back_edge_node.data["depth"] < node.data["depth"]:
                        is_safe_child = True
                        break
                if not is_safe_child:
                    articulation_nodes.append(node)
                    break

        return articulation_nodes
        




    def is_connected(self):
        nodes_found = self.depth_first_traversal(self.nodes[0].id_)
        return len(nodes_found) == len(self.nodes)

    def articulation_nodes_slow(self):
        """
        Return the list of articulation nodes

        for each node:
            remove that node
                if graph is no longer connected
                    that node is an articulation node
        """
        articulation_nodes = []
        for node in self.nodes:
            graph_without_node = copy.deepcopy(self)
            graph_without_node.remove_node(node)
            if not graph_without_node.is_connected():
                articulation_nodes.append(node)
        return articulation_nodes



def main():
    letter_nodes = "ABCDEFGHI"
    list_of_tuple_edges = [
        ("A", "B"), ("A", "C"), ("A", "F"),
        ("B", "D"), ("B", "E"), ("B", "I"), ("B", "G"),
        ("D", "F"), ("D", "G"),
        ("E", "H"), ("E", "I"),
    ]
    graph = Graph()

    for letter_id in letter_nodes:
        node = Node(letter_id)
        graph.add_node(node)

    for start_node, end_node in list_of_tuple_edges:
        graph.add_edge(start_node, end_node)
        graph.add_edge(end_node, start_node)
    
    print(graph)
    pprint.pprint(graph.articulation_nodes_fast())



if __name__ == "__main__":
    main()