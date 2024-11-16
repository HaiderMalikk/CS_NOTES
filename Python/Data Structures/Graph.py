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

* Nodes (the data also known as vertices):
- A, B, C, D, E, F

* Edges (the lines between the nodes connecting them):
- (A, B), (A, C), (A, F)
- (B, C), (B, D), (B, E)
- (C, D), (C, F)
- (D, E)
- (E, F)

* Adjacency Nodes / Neighbors Nodes:
# Node 'x' is a adjacent node of node 'y' if there is an edge from node 'x' to node 'y'. all nodes that connect to 'x' are adjacent nodes of 'x'.
- A: B, C, F -> A has 3 adjacent nodes B, C, F
- B: A, C, D, E
- C: A, B, D, F
- D: B, C, E
- E: B, D, F
- F: A, C

* Path
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
     

* Conectivity
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

* Degree
- in a undirected graph the degree of a node = the number of edges connected to that node. (degree of A in EX1 is 3)
# in a directed graph we have in-degree and out-degree (to keep track of the direction of the edges)
- in-degree of a node = the number of edges that point to that node. (in-degree of A in EX2 is 1)
- out-degree of a node = the number of edges that point from that node. (out-degree of A in EX2 is 1)

* Complete Graph
# A complete graph is a graph where every node is connected to every other node meaning there is a edge between every pair of nodes.
- EX2 is a complete graph beacuse every node is connected to every other node. EX3 is not a complete graph beacuse there is a gap between A and C (no edge)

* Dense vs Sparse Graph
# A dense graph is a graph where the number of edges is close to the maximum number of edges, meaning that almost every pair or all pair of nodes is connected.
# A sparse graph is a graph where the number of edges is much less than the maximum number of edges, meaning that we are near or at the maximum number of edges needed to connect all nodes.

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
- NOTE a directed graph can have some bidirectional edges meaning (A, B) and (B, A) both exist but only (B, C) exists not (C, B)

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

# ! Repersentation of Graphs
# we use this to repersent and store the graph in memory
""" 
# * Adjacency Matrix (building a matrix with EX graphs)
if there is a node from u to v then u is adjacent to v (defenition of adjacency)
a matrix is just a 2d array
so a adjacency matrix is a 2d array that repersents the connections between nodes in a graph in a matrix form

- how to create an adjacency matrix
1) make a kxk matrix where k is the number of nodes in the graph
2) if there is a edge present between the 2 nodes (2 elements in the matrix) then set the value to 1 else set it to 0

EX (undirected and unweighted graph)
      A ------- B
      | \       | \
      |    \    |  E
      |      \  | /
      C ------ D
      
- this will be a 5x5 matrix as we have 5 nodes in the graph, the rows and colums repersent the nodes and the matrix repersents the connections between the 2 nodes with 1s and 0s
- here the lables A-E are not used in the matrix, instead there are just for reference we arrange then in a ordered manner in the matrix
- row 1 and row 2 both conatin all the nodes in the graph A-E where the intersection of any row and column repersents the connection between the 2 nodes in the row and column respectively, 
- if the value is equal to 1 then there is a edge between the 2 nodes if 0 then there is no edge between the 2 nodes
- NOTE how the row and colunm dose not need to have the nodes in order, we can arrange them in any order we want all that matters is that the intersection of the row and column, BUT we need to know how we order the nodes to know which nodes are in the intersection
- NOTE: the nodes in the column repersent the start nodes and the nodes in the row repersent the end nodes here the graph is undirected so A-B = B-A = 1
- EX from matrix: A-A has no edge and hence there intersection is 0, A-B has an edge and hence we give there intersection a value of 1, A-C has an edge and hence we give it a value of 1. ETC

# EX of a Adjecency matrix of the graph above:
  A B C D E
A 0 1 1 1 0
B 1 0 0 1 1
C 1 0 0 1 0
D 1 1 1 0 1
E 0 1 0 1 0


EX (directed graph)
        A <
      /    \ 
     v      \
     B ----> C
- NOTE: the nodes in teh column repersent the start nodes and the nodes in the row repersent the end nodes
- with this info we know that from A-B there is a edge but from B-A there is no edge this will be reflected in the matrix
- EX from matrix: A-B has an edge and hence we give there intersection a value of 1, B-A has no edge and hence there intersection is 0. note how in A->B case the column is A and the row is B and in B->A case the column is B and the row is A.

# EX of a adjecency matrix of the graph above:
  A B C 
A 0 1 1 
B 0 0 1 
C 1 0 0 


EX (weighted graph)
          10
      A ------- B
      | \       | \ 3
    5 |  4 \   7|  E
      |      \  | / 2
      C ------ D   
          1
          
- NOTE: everything is the same but in a weighted graph the value in the matrix repersents the weight of the edge between the 2 nodes not just 1 or 0
- EX from matrix: A-B has an edge with a weight of 10 so the intersection of A(row as A is start) and B(column as B is end) is 10, A-C has an edge with a weight of 5, B-C has no edge and hence there intersection is 0. ETC

  A  B C D E
A 0 10 5 4 0
B 10 0 0 7 3
C 5  0 0 1 0
D 4  7 1 0 2
E 0  3 0 2 0

- if the adjacency matrix has numbers other than 1 and 0 then it is a weighted graph but if it has 0 and 1 then it can be any type of graph


* Implementation of Adjacency Matrix in Python
- can use nested lists to represent the matrix ie 2d array
- we can also use a seprate list to store the nodes in the matrix for reference in the matrix
EX from matrix:
  A B C D E
A 0 1 1 1 0
B 1 0 0 1 1
C 1 0 0 1 0
D 1 1 1 0 1
E 0 1 0 1 0

node list: ['A', 'B', 'C', 'D', 'E'] # index 0-4 repersents the node A-E respectively

EX of nested list repersentation:
- here we have a 2d array ie matrix that has all the values from the adjacency matrix
- each subarray repersents a row
- here we can use the index of every element to dertermine the start and end nodes of the edge by mapping each index of the row or column to the index of the node list
- EX from nested list repersentation: node at index 0 in the colunm or 0 index in the row is A beacuse A is at index 0 in the node list
- just like this the outer index is the column and the inner index is the row where the index of row or column is the index of the node list 
- we start from the column index and end at the row index, as we go from column node to row node
- EX: at index[0][1] we have A-B as the column index(starting node) is 0 = A and the row index(end node) is 1 = B, so A-B has an edge and the value in the matrix is 1
- EX: at index [1][3] we have B-D the outer index is the column and the inner index is the row so B-D has an edge and the value in the matrix is 1
- NOTE while the nested list's is a list of rows the index repersents the column while the the row is the index of a element within the subarray
[
    [0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

# Problem with adjacency matrix: we store too many 0's for a sparse graph why do we need to store the value of a edge between 2 nodes if they dont have an edge (Matrixs are expensive to store) so we use:


* Adjacency List (Building a list with EX graphs)
- this makes it more efficient to store sparse graphs
- In adjacency list we create a list for each node in the graph, this list contains all the nodes that are adjacent to the node meaning connected to the node
- EX from graph (undirected and unweighted graph):
# graph:
      A ------- B
      | \       | \
      |    \    |  E
      |      \  | /
      C ------ D

- creating a list for each nodes adjacent nodes:
- A: [B, C, D]
- B: [A, D, E]
- C: [A, D]
- D: [A, B, C, E]
- E: [B, D]

# EX from graph (directded and unweighted graph):
        A <
      /    \ 
     v      \
     B <---> C
     
- Adjacency list (keeping track of direction):
A: [B]
B: [C]
C: [B, A]

# EX from graph (undirected and weighted graph):
           5
      A ------- B
      | \       | \ 3
    4 |  10\   1|  E
      |      \  | / 2
      C ------ D   
          7

- Adjacency list (keeping track of weight using a key value pair where the key is the adjacent node and the value is the weight, you can use hashmap or tuple pairs in the list ETC):
A: [(B, 5), (C, 4), (D, 10)] 
B: [(A, 5), (D, 1), (E, 3)]
C: [(A, 4), (D, 7)]
D: [(A, 10), (B, 1), (C, 7), (E, 2)]
E: [(B, 3), (D, 2)]

* Adjacency Matrix implementation in Python:
# we can use a dictionary or (hashmap) to store the adjacency list, where the key is the node and the value is the list of adjacent nodes 
# if the nodes have weights we can use a nested dictionary where the key is the node and the value is a dictionary where the key is the adjacent node and the value is the weight
- EX: { A: [B, C, D] } here A is the key and [B, C, D] is the value which is a list of adjacent nodes
- EX: { A: { B: 5, C: 4, D: 10 } } here A is the key and the values are another dictionary where the key is the adjacent node and the value is the weight
"""
