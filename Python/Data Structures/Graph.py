# ! Graphs 

# Graph is a non -linear data structure consisting of nodes or vertices connected by edges. nodes and vertices are the same thing
# a edge can only connect 2 nodes its a stright line between 2 nodes
# NOTE: a tree is a type of graph. but not all graphs are trees. a tree is a graph with no cycles.
# a tree has a root and each child can have only 1 parent but not all graphs have a root. and a node can have multiple parents in a graph. with multiple paths to the same node.
# a graph can have cycles. a cycle is when a node is connected to itself . or a node is connected to another node which is connected to another node which is connected to the same node.
# ! EX OF GRAPHs
# EX1 (undirected graph)
""" 
          A ------- B
         / |      / | \
        F  |    /   |  E
         \ | /      | /
           C ------ D

Nodes (the data also known as vertices):
- A, B, C, D, E, F

Edges (the lines between the nodes connecting them):
- (A, B), (A, C), (A, F)
- (B, C), (B, D), (B, E)
- (C, D), (C, F)
- (D, E)
- (E, F)

Adjacency Nodes / Neighbors Nodes:
# Node 'x' is a adjacent node of node 'y' if there is an edge from node 'x' to node 'y'. all nodes that connect to 'x' are adjacent nodes of 'x'.
- A: B, C, F -> A has 3 adjacent nodes B, C, F
- B: A, C, D, E
- C: A, B, D, F
- D: B, C, E
- E: B, D, F
- F: A, C

Path
# a Path is a squence of nodes where each next node is connected to the previous node by an edge 
# NOTE: we take into account the direction of the edge connecting the nodes. (see connectivity for more info on direction)
- A -> B -> C -> D -> E (Path from A to E)
- To get the length of a path, we count the number of edges in the path. A-E in the last example is length of 5, (len != 0 in a path)
- In a simple path, no node or edge is repeated.  
- In a closed path, the first and last node are the same. 
- A cycle is a path where the first and last node are the same. a cycle can be a simple path or not.
- ETC

# Ex of graphs for connectivity (both directed graphs)
# EX2
        A <
      /    \ 
     v      \
     B ----> C
     
# EX3
        A 
      /     
     v      
     B ----> C
     

Conectivity
# A graph is connected if there is a path between every pair of nodes. so there is a path from any node to any other node.
- our graph is connected because there is a path from any node to any other node.
- in a unconnected graph the graph will have a disconnected path between any 2 nodes meaning a gap between the nodes where no edge connects them.
- A Strongly Connected Graph (SCG) is a graph where there is a path from any node to any other node for all nodes.
- A Weakly Connected Graph (WCG) is a graph where there is not a path from every node to every other node meaning you cannot get from node 'x' to node 'y' and vice versa for a certain pair of nodes.
- a SCG or WGC has to be connected as connectivity dose not apply to disconnected graphs. 
- if a graph is undirected then its a SCG.
- A directed graph is strongly connected (SCG) if there is a directed path from every node to every other node.
- If a directed graph does not have such two-way paths for all node pairs but becomes strongly connected when edge directions are ignored, it is weakly connected (WCG).
- EX1 is a SCG beacuse there is a path from any node to any other node. (its a undirected graph)
- EX2 is a SCG and a directed graph beacuse there is a path from any node to any other node and the edges are directed.
- EX3 is a WCG and a directed graph beacuse there is not a path from any node to any other node but when the edges direction is ignored it becomes a SCG so its a WCG

Degree
- in a undirected graph the degree of a node = the number of edges connected to that node. (degree of A in EX1 is 3)
# in a directed graph we have in-degree and out-degree (to keep track of the direction of the edges)
- in-degree of a node = the number of edges that point to that node. (in-degree of A in EX2 is 1)
- out-degree of a node = the number of edges that point from that node. (out-degree of A in EX2 is 1)

Complete Graph
# A complete graph is a graph where every node is connected to every other node meaning there is a edge between every pair of nodes.
- EX2 is a complete graph beacuse every node is connected to every other node. EX3 is not a complete graph beacuse there is a gap between A and C (no edge)

NOTE: that for EX1) A->B is the same as B->A here so we dont mention B->A only A->B. and this is the same for all edges like this.
"""


# ! Mathamatical Representation of Graphs
""" 
G = {V, E} 
where V is the set of vertices (V = {A, B, C, D, E, F}), 
E is the set of edges (E = {(A, B), (A, C), (A, F), (B, C), (B, D), (B, E), (C, D), (C, F), (D, E), (E, F)}
G is the graph itself
- using "()" repersents a ordered pair . and using "[]" represents an unordered pair. our example is an unordered pair or unidirected graph as A -> B is the same as B -> A and etc
"""

# ! Types of Graphs

# * ordered vs unorderd pairs (undirected vs directed graph)
""" 
Unordered Pairs (Undirected Graph)
In an undirected graph, edges are represented as unordered pairs.
This means that the edge (A, B) is the same as (B, A).
There is no direction associated with the edges, so traveling from A to B is the same as traveling from B to A.
This property must be true for all edges in an undirected graph.
Example: edges = {('A', 'B'), ('A', 'C'), ('B', 'C')} # Edge (A, B) is identical to (B, A).

Ordered Pairs (Directed Graph)
In a directed graph (digraph), edges are represented as ordered pairs.
This means that (A, B) is not the same as (B, A); (A, B) implies a one-way connection from A to B.
This property must be true for all edges in a directed graph.
Example: edges = [('A', 'B'), ('B', 'C')] # Edge (A, B) represents a direction from A to B only.

- Both types can have cycles.
"""

# * weighted vs unweighted graph
""" 
Weighted Graphs
In a weighted graph, edges are represented with a weight associated with them.
This weight can be a numerical value, a string, or any other type of data.
Weighted graphs are useful for modeling real-world scenarios where edges have different costs or weights.
Example: edges = [('A', 'B', 5), ('B', 'C', 3), ('C', 'D', 2)] # Edge (A, B) has a weight of 5.

Unweighted Graphs 
In an unweighted graph, edges are represented without a weight associated with them.
This means that there is no numerical value associated with the edges.
Unweighted graphs are useful for modeling scenarios where edges have no specific cost or weight.
Example: edges = [('A', 'B'), ('B', 'C'), ('C', 'D')] # Edge (A, B) has no weight.
"""

# * Cyclic vs Acyclic Graphs
""" 
Cyclic Graphs
In a cyclic graph, there are cycles (or loops) in the graph.
This means that there is a path from any node to itself.
Cyclic graphs are useful for modeling scenarios where there is back-and-forth movement.
Example: edges = [('A', 'B'), ('B', 'C'), ('C', 'A')] # There is a cycle from A to A.

Acyclic Graphs
In an acyclic graph, there are no cycles (or loops) in the graph.
This means that there is no path from any node to itself.
Acyclic graphs are useful for modeling scenarios where there is no back-and-forth movement.
Example: edges = [('A', 'B'), ('B', 'C'), ('C', 'D')] # There is no cycle from A to A.
"""

# ! uses of Graphs
# Graphs are used to represent relationships between objects, such as a social network or a file system.
# Graphs can be used to model real-world problems, such as finding the shortest path between two cities or the minimum spanning tree of a network.

