# Graphs 

# Graph is a non -linear data structure consisting of nodes or vertices connected by edges. nodes and vertices are the same thing
# a edge can only connect 2 nodes its a stright line between 2 nodes
# NOTE: a tree is a type of graph. but not all graphs are trees. a tree is a graph with no cycles.
# a tree has a root and each child can have only 1 parent but not all graphs have a root. and a node can have multiple parents in a graph. with multiple paths to the same node.
# a graph can have cycles. a cycle is when a node is connected to itself . or a node is connected to another node which is connected to another node which is connected to the same node.
# EX OF GRAPHs
""" 
          A ------- B
         / |      / | \
        F  |    /   |  E
         \ | /      | /
           C ------ D

Nodes:
- A, B, C, D, E, F

Edges (the lines between the nodes):
- (A, B), (A, C), (A, F)
- (B, C), (B, D), (B, E)
- (C, D), (C, F)
- (D, E)
- (E, F)

there are many paths between 2 nodes in a graph. EX: f to E is F -> C -> D -> E or F -> A -> B -> E
A cycle (or loop) is a path that starts and ends at the same node. here a cycle is A -> B -> D -> C -> A
"""

# orderd un orderd pairs and undirected vs directed graph
""" 
Unordered Pairs (Undirected Graph)
In an undirected graph, edges are represented as unordered pairs.
This means that the edge (A, B) is the same as (B, A).
There is no direction associated with the edges, so traveling from A to B is the same as traveling from B to A.
Example: edges = {('A', 'B'), ('A', 'C'), ('B', 'C')} # Edge (A, B) is identical to (B, A).

Ordered Pairs (Directed Graph)
In a directed graph (digraph), edges are represented as ordered pairs.
This means that (A, B) is not the same as (B, A); (A, B) implies a one-way connection from A to B.
Example: edges = [('A', 'B'), ('B', 'C')] # Edge (A, B) represents a direction from A to B only.

- Both types can have cycles.
"""

# Mathamatical Representation of Graphs
""" 
G = {V, E} 
where V is the set of vertices (V = {A, B, C, D, E, F}), 
E is the set of edges (E = {(A, B), (A, C), (A, F), (B, C), (B, D), (B, E), (C, D), (C, F), (D, E), (E, F)}
G is the graph itself
- using "()" repersents a ordered pair . and using "[]" represents an unordered pair. our example is an unordered pair or unidirected graph as A -> B is the same as B -> A and etc
"""

# Graphs are used to represent relationships between objects, such as a social network or a file system.
# Graphs can be used to model real-world problems, such as finding the shortest path between two cities or the minimum spanning tree of a network.
