class Graph:
    def __init__(self, graph_list=None):
        if graph_list is None:
            graph_list = {}
        self.graph_list = graph_list
    
    def add_node(self, node):
        if node in self.graph_list:
            print(f"Node {node} already exists in the graph")
        else:
            self.graph_list[node] = []
    
    def add_edge_undirected(self, node1, node2, weight=1):
        if node1 not in self.graph_list or node2 not in self.graph_list:
            print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
        else:
            self.graph_list[node1].append((node2, weight))
            self.graph_list[node2].append((node1, weight))
            
    def add_edge_directed(self, node1, node2, weight=1):
        if node1 not in self.graph_list or node2 not in self.graph_list:
            print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
        else:
            self.graph_list[node1].append((node2, weight))
            
    def print_graph(self):
        print("{")
        for node, edges in self.graph_list.items():
            edges_str = ", ".join([f"('{adj_node}', {weight})" for adj_node, weight in edges])
            print(f"    '{node}': [{edges_str}],")
        print("}")
        
    def delete_node(self, node):
        if node not in self.graph_list:
            print(f"Node {node} does not exist in the graph")
        else:
            self.graph_list.pop(node)
            for key in self.graph_list:
                current_nodes = self.graph_list[key]
                for adjacent_node in current_nodes:
                    if adjacent_node[0] == node:
                        current_nodes.remove(adjacent_node)
    
    def delete_edge(self, node1, node2):
        if node1 not in self.graph_list or node2 not in self.graph_list:
            print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
        else:
            for adjacent_node in self.graph_list[node1]:
                if adjacent_node[0] == node2:
                    self.graph_list[node1].remove(adjacent_node)
            
            for adjacent_node in self.graph_list[node2]:
                if adjacent_node[0] == node1:
                    self.graph_list[node2].remove(adjacent_node)
                    
    def DFS(self, start_node=None):
        visited = set() 
        
        if start_node is None:
            start_node = list(self.graph_list.keys())[0] 
        
        self.DFS_recursive(start_node, visited)
    def DFS_recursive(self, start_node, visited):
        if start_node is None:
            start_node = list(self.graph_list.keys())[0]
        
        if start_node not in self.graph_list:
            print("Start node not in graph")
            return
        
        if start_node not in visited:
            print(start_node)
            visited.add(start_node)
            for adjacent_node in self.graph_list[start_node]:
                self.DFS_recursive(adjacent_node[0], visited)
                
    def BFS(self, start_node=None):
        visited = set()  
        queue = []

        if start_node is None:
            start_node = list(self.graph_list.keys())[0]  

        queue.append(start_node)  
        self.BFS_recursive(queue, visited)

    def BFS_recursive(self, queue, visited):
        if not queue:  
            return
        current = queue.pop(0)  
        if current not in visited:  
            print(current)  
            visited.add(current)  
            for adjacent_node in self.graph_list[current]:  
                if adjacent_node not in visited:
                    queue.append(adjacent_node[0])
                    
        self.BFS_recursive(queue, visited)
        
