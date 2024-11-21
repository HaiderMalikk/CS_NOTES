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

# ! Repersentation of Graphs NOTE: for us the adjacency lists nodes have there adjacent nodes in the format (node, weight) where this node is adjacent to the node
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
# NOTE: the letters are just for reference and are not used in the matrix
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

# ! Implementing Graphs in Python

# ! Insertion Operations (Adding Nodes and Edges to the Graph -> Theory)
# used to insert a new node or edge into the graph

# * Add node / vertex (no edge just the node)
# first we need to check if the node already exists in the graph if false: addnode
# after adding the node the graph will be disconnected, the number of nodes is increased by 1 but edges is the same as before
# in a adjacency matrix we add a new row and column for the new node but the value for the new nodes intersection with any node is 0 (no edge)
# in a adjacency list we create a new key in the dictionary and assign it an empty list as the value this will store the edges for the new node later
# adding a new node to a directed/undirected graph will also create a disconected graph as there is no edge direction yet we add this to the list or matrix 
# for a weighted graph when we add a new node we add a key to the dictionary and assign it an empty dictionary as we need to store the adjecency nodes (keys) and the weights (values) for the new node, for matrix we just add the value to the matrix
# we can add the node like this: add_node('F'), then in the matrix we add the row and column by adding the node to our nodes list and adding a new row and incresing all the columns by 1 and filling the new position with 0s, for the adjecent list we do: graph['F'] = [] and for the weighted graph we do: graph['F'] = {}, where graph is the graph dictionary

# * Add edge (we check and verify that nodes A and B exist in the graph)
# when we add a new edge we need to specify 2 nodes and the edge is repersented by a value not a physical line
 
# in a undirected and unweighted graph we add the edge mention 2 nodes to connect: We first check if the nodes exist if true we add the edge, add_edge(A, B)
# in the matrix we need to update the matrix by adding the value to the matrix at the intersection of the 2 nodes (since its undirected we have 2 intersections A-B and B-A): matrix[A][B] = 1, matrix[B][A] = 1 where A and B are the nodes we want to connect
# in the adjacency list we do: graph[A] = [B] and graph[B] = [A] where A and B are the nodes we want to connect (undirected so we do both)

# in a directed and unweighted graph we can mention the strating node first then the end node: add_edge(A, B) this connects A to B only, we still must check if the nodes exist before adding the edge
# in the matrix we need to update the matrix by adding we to the intersection of the 2 nodes: matrix[A][B] = 1 where A is the stating node (in the column) and B is the end node (in the row)
# in the adjacency list we do: graph[A] = [B] where A is the stating node and B is the end node (directed so only one way A-B) so leave the value of key B as it is 

# in a Weighted undirected graph we mention the two nodes to connect and the edge weight: add_edge(A, B, weight)
# in the matrix we need to update the matrix by adding the value to the matrix at the intersection of the 2 nodes (since its undirected we have 2 intersections A-B and B-A): matrix[A][B] = weight, matrix[B][A] = weight where A and B are the nodes we want to connect and the weight is the value we want to assign to the edge
# in the adjacency list we do: graph[A] = { B: weight } and graph[B] = { A: weight } where A and B are the nodes we want to connect (undirected so we do both)

# ! Creating Graph Using Adjacency Matrix
# python code using info above to implement the insertion operations
# * Creating a Graph as a martrix 
# we will implement the graph here
# this is a directed and weighted graph where there is no weight its 1 (default) and where theres no direction its undirected
""" 
graph:
      A ------- B
      | \       | \
    5 |    \    |  E
      |      \  | /
      C ------> D
Adjacency Matrix in matrix form:
[   A  B  C  D  E
 A [0, 1, 5, 1, 0],
 B [1, 0, 0, 1, 1],
 C [5, 0, 0, 1, 0],
 D [1, 1, 0, 0, 1],
 E [0, 1, 0, 1, 0]
]
Nodes list: ['A', 'B', 'C', 'D', 'E'] # index 0-4 repersents the node A-E respectively meaning at [0][1] we have A(col)->B(row)
"""
# * creating the graph
nodes = []
graph_matrix = [] # we will ad the inner list later
node_count = 0 # the number of nodes in the graph

# * Adding a node to the graph
def add_node(node): # function to add a new node to the graph
  global node_count # to use node_count inside the function as we are modifying it # NOTE: for list types we need to use global
  # check if the node already exists in the graph
  if node in nodes:
    print(f"Node: {node} already exists in the graph")
    return
  else:
    nodes.append(node)
    node_count += 1
    # now we must add a extra column to all the inner lists (rows) in the graph_matrix + add a new inner list(row) to the end of the graph_matrix
    # # we can do this with a for loop appending a empty element to the end of each inner list in the graph_matrix then adding a new list as inner list to graph but first lopping over node_count many times to add 0s to this new inner list (row)
    # NOTE: we only add 0's as we only adds nodes here not edges
    for n in graph_matrix: # adding the column by adding an empty element to the end of each inner list
      n.append(0) # append always adds to the end of the list
    
    temp_list = [] # create a new list to add to the end of the graph_matrix we will add the value of 0 in this temp list n times where n is the number of nodes = node count, NOTE: we alredy incemented the node count to account for the added node i.e to account for the new column
    for i in range(node_count): # add a new inner list to graph_matrix with the length of the number of nodes in the graph = nodecount (filled with zeros as we are only adding a node and no edges exist yet thats for add egde )
      temp_list.append(0)
    graph_matrix.append(temp_list) # add the new filled list to the end of the graph_matrix using append method which adds to the end of the list

# * adding edges to the graph (undirected and weighted or unweighted)
# adding edges to the graph using the adjacency matrix
def add_edge_undirected(node1, node2, weight = 1): # function to add an edge to the graph, takes in two nodes and the weight of the edge which defaults to 1
  if node1 not in nodes or node2 not in nodes: # check if both nodes exist in the graph
    print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
    return
  else: # add the edge
    # to add the dge we need to add the weight to the matrix at the intersection of the 2 nodes where first node1 is the column(inner index) and node2 is the row(outer index)
    # then node2 is the column(inner index) and node1 is the row(outer index) to make it a undirected graph.
    indexnode1 = nodes.index(node1) # get the index of the node1 using the index method
    indexnode2 = nodes.index(node2) # get the index of the node2 using the index method
    graph_matrix[indexnode1][indexnode2] = weight # add the edge by setting the value at the intersection of the two nodes to the weight
    graph_matrix[indexnode2][indexnode1] = weight # add the edge by setting the value at the intersection of the two nodes the other way around to make it a undirected graph
    # now we have a undirected unweighted edge between the two nodes
    # NOTE: here we dont check to see if edge exists as thats not needed also in a weighted graph we can update the weight (edge value)

# * adding edges to the graph (directed weighted or unweighted) 
# all we need to cahnge is to only add the egde in one direction from node 1 to node 2
# this means we only take node 1 as the column(inner index) and node 2 as the row(outer index)
def add_edge_directed(node1, node2, weight = 1): # add edge from node 1 to node 2, default weight is 1
  if node1 not in nodes or node2 not in nodes: # check if both nodes exist
    print(f"One or both nodes: {node1}, {node2} do not exist in the graph") # print the error message
    return
  else: # add the edge
    indexnode1 = nodes.index(node1) # get the index of the node1 using the index method
    indexnode2 = nodes.index(node2) # get the index of the node2 using the
    graph_matrix[indexnode1][indexnode2] = weight # add the edge by setting the value at the intersection of the two nodes to the weight
    # Only do this from node 1 to node 2 to create a directed edge for directed graph

# * printing graph 
# if we just print the graph matrix it will print it in a linear format but we want a matrix format
# NOTE  this can easily and iffeciently be solved insode the add node method but we will do it here for clarity
# we also add node headers for readability
def print_graph(): # function to print the graph
# Print column headers
  print("  ", end="")  # Indent for the row headers
  for node in nodes: # loop over the nodes to print the node headers in there respective columns
      print(node, end=" ") # print the node name in the current column and 'end' makes it so all the nodes in the column are printed on the same line
  print() # print a new line after each row i.e after end of loop for column
    
  for i in range(node_count): # loop over the number of nodes for the number of rows
    print(nodes[i], end=" ")  # Print the row header in the current row
    for j in range(node_count):  # loop over the number of nodes for the number of columns
      print(graph_matrix[i][j], end=" ") # print the value at the current row and column the end ensures the column is printed on the same line
    print() # print a new line after each row i.e after end of loop for column

# * adding nodes to the graph using add_node (can be done in a loop)
# creating nodes to add to graph matrix to create the graph above 
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("A") # test adding a node that already exists

# * adding edges to the graph using add_edge methods (we can create directed and undirected graphs with both weighted and unweighted edges)
# creating edges between nodes we just added previously to create the Example graph above
add_edge_undirected("A", "B") # no need to do add_edge_undirected_unweighted("B", "A") since its a undirected graph (has default weight of 1)
add_edge_undirected("A", "C", 5) # test adding a weighted edge
add_edge_undirected("A", "D")
add_edge_undirected("B", "D")
add_edge_directed("C", "D") # test adding a directed edge weight is 1
add_edge_undirected("E", "B")
add_edge_undirected("E", "D")
add_edge_undirected("A", "R") # test adding an edge between nodes that dont exist

# * printing the graph using print_graph 
# creating a adjacency matrix of the graph EX above with added nodes and edges 
# if we had to nodes the graph would be empty if we had no egdes the graph would have rows and columns for the nodes but all values would be 0
print_graph() # print the graph matrix

# ! Creating Graph Using Adjacency List (we use tuples to store each nodes adjacent nodes and there weights but can also use a nested dictionary to store the adjacent nodes and their weights)
# Creating a graph using adjacency list
# EX graph to implement using adjacency list
""" 
# graph (undirected and unweighted graph):
      A ------- B
      | \       | \
    5 |    \    |  E
      |      \  | /
      C ------> D

- creating a list for each nodes adjacent nodes:
{
    'A': [('B', 1), ('C', 5), ('D', 1)],
    'B': [('A', 1), ('D', 1), ('E', 1)],
    'C': [('A', 5), ('D', 1)],
    'D': [('A', 1), ('B', 1), ('E', 1)],
    'E': [('B', 1), ('D', 1)],
}
"""
# we will use dictionary to store the adjacency list where the key is the node and the value is the list of adjacent nodes
# in a weighted graph we will use a tuple to store the adjacent node and the weight of the edge
# we can also use a nested dictionary where the key is the node and the value is a dictionary where the key is the adjacent node and the value is the weight (see notes for more)
# by using a a empty list and tuples insted of a nested dictionary we can use the same code for both unweighted and weighted graphs
# * creating the graph
graph_list = {} # dictionary to store the adjacency list

# * adding nodes to the graph using add_node (can be done in a loop)
def add_node(node): # function to add a node to the list (weighted and unweighted)
  if node in graph_list: # first check if the node already exists in the graph if false: addnode if true do nothing;
    print(f"Node {node} already exists in the graph")
    return # we are done
  else: # else add the node
    # when adding the node we only add the node and no edge so all we do is add the node as a key to the dictionary with an empty list as the value
    graph_list[node] = [] # add the node as a key to the dictionary with an empty list as the value
    
# * adding edges to the graph (undirected and weighted or unweighted) 
def add_edge_undirected(node1, node2, weight=1): # function to add an edge to the graph, takes in two nodes and the weight of the edge which defaults to 1
  if node1 not in graph_list or node2 not in graph_list: # first check if the nodes exists in the graph if false: add egde if true do nothing;
    print(f"Node {node1} or {node2} does not exist in the graph")
    return # we are done
  else: # else add the edge
    # when adding the edge we only add the edge and no node so all we do is add the node1 as a value to the node2 key in the dictionary and vice versa since the graph is undirected
    graph_list[node1].append((node2, weight)) # add the node1 as a value to the node2 key in the dictionary
    graph_list[node2].append((node1, weight)) # add the node2 as a value to the node1 key in the dictionary
    # NOTE: the weight is added as a along with node but is optional if no weight is provided it will default to 1

# * adding edges to the graph (directed and weighted or unweighted)
def add_edge_directed(node1, node2, weight=1): # function to add an edge to the graph, we go from node 1 to node 2, default weight of the edge which defaults to 1
  if node1 not in graph_list or node2 not in graph_list: # first check if
    print(f"Node {node1} or {node2} does not exist in the graph")
    return # we are done
  else: # else add the edge
    # when adding the edge we only add the edge and no node so all we do is add the node1 as a value to the node2 key in the dictionary since the graph is directed
    graph_list[node1].append((node2, weight)) # add the node1 as a value to the node2 key in the dictionary
    # NOTE: the weight is added as a along with node but is optional if no weight is provided it will default to 1
    
# * printing the graph using print_graph (optional just makes graph easier to read)
# * Method to print the graph in the desired format
# * Method to print the graph in the requested format
# * Method to print the graph in a compact format
def print_graph():
    print("{")
    for node, edges in graph_list.items():
        # Format edges compactly
        edges_str = ", ".join([f"('{adj_node}', {weight})" for adj_node, weight in edges])
        print(f"    '{node}': [{edges_str}],")
    print("}")

    
# Note the nodes can be string , int, float, etc. as long as they are hashable
# * adding nodes to the graph
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
# add_node("A") # test adding a node that already exists will print a message and do nothing

# * adding edges to the graph 
add_edge_undirected("A", "B") # note thta since its undirected node A gets B and node B gets A in the adjacency list
add_edge_undirected("A", "C", 5) # undirected edge with weight 
add_edge_undirected("A", "D") 
add_edge_undirected("B", "D")
add_edge_directed("C", "D") # directed edge
add_edge_undirected("E", "B")
add_edge_undirected("E", "D")

# * printing the graph 
print_graph() # prints the graph in the desired format

# ! Delete a node from a graph
# Deleting a node will delete that node from the graph and delete all edges connecting to that node NOTE: the edges direction dose not matter 
# EX from graph (undirectded and unweighted graph):
""" 
         A      D
       /   \   /
      /     \ /
     B ----- C
     
- Adjacency Matrix: 
Nodes: [A, B, C, D]

    A  B  C  D    
A [[0  1  1  1], 
B  [1  0  1  0],
C  [1  1  0  1],
D  [0  0  1  0]]
  
- Adjacency list:
{ 
A: [(B, 1), (C, 1)]
B: [(A, 1), (C, 1)]
C: [(A, 1), (B, 1), (D, 1)] 
D: [(C, 1)]
}

# EX: lets delete C by calling delete_node(C)
1)
# we call our function for deleting where we input c as the argument

2)
# For the matrix we need to delete every node at the index of C in every row(subarray) this deletes the column for the row we delete the whole subarray at index of C
# for the list we need to delete the nested list with key C, but since all other keys (nodes) will have another key value pair(dictinary) with key as node and value as weight or a tuple with (Node, weight).
# for the nested tuples we serch it i.e we serch the nodes adjacent nodes and find the key of C which is alwasy the first index in this tuple inside nested list, and simply delete it, since the values of that key C are the weights of the edges connecting to C we remove all the egdes by deleting Key C
# For the nested dictionary each node has a nested dictionary with keys and values, we serch all nodes in this adjectent nodes dictionary and find the key of C and delete it 
# in both cases for the list and matrix we delete the node and in doing so all the edges connecting to that node are deleted

Done)
# after deleting C from the graph:
         A      D
       /       
      /       
     B
# note how now teh graph is disconected
- Adjacency Matrix: 
Nodes: [A, B, D]

    A  B  D    
A [[0  1  1], 
B  [1  0  0],
D  [0  0  0]]
  
- Adjacency list:
{ 
A: [(B, 1)],
B: [(A, 1)]
D: []
} 
"""

# ! Delete an edge from a graph
# This is not the same as deleting a node from the graph we can delete an edge and still have the nodes in the graph
# deleting the edge will just delete the value of the weight of that edge from the matrix and list by deleting we set the value to 0
# EX:
""" 
graph:
           4
      A -------> B
      | \       | \ 
      |    \    |  E
      |      \  | /
      C---------D
Adjacency Matrix in matrix form:
[   A  B  C  D  E
 A [0, 4, 1, 1, 0],
 B [0, 0, 0, 1, 1],
 C [1, 0, 0, 1, 0],
 D [1, 1, 1, 0, 1],
 E [0, 1, 0, 1, 0]
]
Nodes list: ['A', 'B', 'C', 'D', 'E'] # index 0-4 repersents the node A-E respectively meaning at [0][1] we have A(col)->B(row)

Adjacency List
{
     A: [(B, 4), (C, 1), (D, 1)],  
     B: [(A, 0), (D, 1), (E, 1)],
     C: [(A, 5), (D, 1)]
     D: [(A, 1), (B, 1), (E, 1)],
     E: [(B, 1), (D, 1)]
}

# NOTE: The direction of the edge does not matter for deleting an edge EX: if the graph was C-D only D-C would be 0 by deting the edge C-D would be 0 but D-C would still be 0 so its like deleting a empty value.
# also the weight of the edge dose not matter as after deleting the edge the weight will be 0 in the matrix and list
# SO, Deleted edge between two nodes = 0, in graph and list, # for directed or undirected graph the deletion is the same as we delete the egde regardless of the direction

1) lets delete a edge from the graph by calling the delete_edge_(C, D) # where C and D are two nodes and the edge direction does not matter 
# we will delete the edge between C and D by setting the value of the edge to 0 in the matrix and list but we need to find the two nodes first
# in the matrix we will delete the value at the row of C and the column of D and vice versa, so we say: matrix[C][D] = 0 and matrix[D][C] = 0
# if the edge in the matrix is directed say C-D then matric[D][C] = 0 and setting it to 0 has no affect so we can group the two types of edges together
# in the list we will delete the value of the edge between C and D by removing the key D from the list of C and removing the key C from the list of D
# because list holds only adjacent nodes after deleting the edge C-D or D-C (dose not matter) 
# the value of D in adjacent list of C will be 0 and the value of C in adjacent list of D will be 0
# once again like the matrix we can ignore if the edge is directed or undirected if its directed from C-D then the node is in C's list, we remove it and from D's list C was never there so we dont need to remove it
# so basically in list we find key C in graph and serch key C find adjacent node D and remove it and then find key D in graph and search key D find adjacent node C and remove it
# by remove it i mean remove the whole tuple or remove the whole key form the adjacent nodes list for both keys C and D, NOTE: since theres no edge between C and D none of these 2 are adjacent to each other hence why we can remove them from the list

# After deleting the edge:
graph:
           4
      A ------> B
      | \       | \
      |    \    |  E
      |      \  | /
      C         D
Adjacency Matrix in matrix form:
[   A  B  C  D  E
 A [0, 4, 1, 1, 0],
 B [0, 0, 0, 1, 4],
 C [5, 0, 0, 0, 0],
 D [1, 1, 0, 0, 1],
 E [0, 1, 0, 1, 0]
]
Nodes list: ['A', 'B', 'C', 'D', 'E'] # index 0-4 repersents the node A-E respectively meaning at [0][1] we have A(col)->B(row)

Adjacency List
{
     A: [(B, 4), (C, 1), (D, 1)],  
     B: [(A, 0), (D, 1), (E, 1)],
     C: [(A, 5)],
     D: [(A, 1), (B, 1), (E, 1)],
     E: [(B, 1), (D, 1)]
}
"""
# * All methods below are for weighted / unweighted / directed / undirected graphs graphs
# * Creting a method to Delete a node for Adjacency Matrix
# NOTE: for this example i will define the methods fand graph and wont define extra functions 
nodes = [] # to hold the nodes of the graph
graph_matrix = [] # matrix to hold the graph
node_count = 0 # the number of nodes in the graph
def delete_node(node):
  global node_count # to use node_count inside the function as we are modifying it # NOTE: for list types we need to use global
  if node not in nodes:
    print(f"Node: {node} does not exist in the graph")
    return
  else:
    indexofcolumn = nodes.index(node) # get the index of the node in the nodes list this = the index of the node column/row in the matrix where the node is we delete every element in all column at this index and the row at this index
    nodes.remove(node) # remove the node from the nodes list (which holds all the nodes in the graph) 
    node_count -= 1 # decrease the number of nodes in the graph by 1
    graph_matrix.pop(indexofcolumn) # delete the row of the node from the matrix NOTE the graphs column index = its row index see the graph matrix above for reference
    for column in graph_matrix:
      column.pop(indexofcolumn) # delete the index of the node from every column in the matrix all elements of node in the column will be deleted
      # NOTE: no shifting of columns is required because pop and remove adjust the list for us so theres no gaps in the matrix
# delete_node("C") # ex

# build a matric graph using the code above then call the delete_node function to delete a node the results of this are in the doc string above
# * Creating a method to Delete a edge for Adjacency Matrix
def delete_edge(node1, node2): # takes in two nodes once again the direction of the edge does not matter
  if node1 not in nodes or node2 not in nodes: # if either of the nodes do not exist in the graph
    print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
    return # we are done
  else: # if both nodes exist in the graph
    indexnode1 = nodes.index(node1) # get the index of the first node in the nodes list 
    indexnode2 = nodes.index(node2) # get the index of the second node in the nodes list
    graph_matrix[indexnode1][indexnode2] = 0 # set the value at the intersection of the two nodes to 0 wher the column is the first node and the row is the second node
    graph_matrix[indexnode2][indexnode1] = 0 # set the value at the intersection of the two nodes to 0 wher the column is the second node and the row is the first node
    # NOTE: this is the same is saying node1's col and node2's row = 0 and node2's col and node1's row = 0 which deletes both edges node1->node2 and node2->node1 
    # if its directional one of the above lines wall be 0 anyway and its like saying 0 = 0 so its ok
    
# delete_edge("C", "D") # ex

# * Creating a method to Delete a node for Adjacency List (by cheking if the node exits we can safely delete it) adjecency nodes must be in format (adjacent node, weight) !!!
# note again the fomat of the adjacency nodes in the adjacency list of every node is (adjacent node, weight)
graph_list = {} # dictionary to store the adjacency list

def delete_node(node):
  if node not in graph_list:
    print(f"Node: {node} does not exist in the graph")
    return
  else:
    # here we have to go through every node to find if node in graph is adjacent to the node we are deleting
    graph_list.pop(node) # remove the node from the graph list this will delete the whole key (node) and all its values (adjacent nodes) from the dictionary
    for key in graph_list: # iterate over the keys in the graph list the keys are all the nodes in the graph
      current_node = graph_list[key] # current node is the value of the key (node) in the graph list that we are looking at
      for adjacent_node in current_node: # iterate over the adjacent nodes of the current node 
        if adjacent_node[0] == node: # if the adjacent node is the node we are deleting
          current_node.remove(adjacent_node) # remove the adjacent node from the current node's adjacent nodes list this removes the whole tuple (adjacent node, weight) from the list deleting the node and its edges as the egde is the weight
        
# delete_node("C") # ex

# * Creating a method to Delete a edge for Adjacency List (by cheking if the node exits we can safely delete it)
def delete_edge(node1, node2):
  if node1 not in graph_list or node2 not in graph_list:
    print(f"One or both nodes: {node1}, {node2} do not exist in the graph")
    return
  else:
    # here we can break once we find the adjacent node in the node we are looking as we are deleting the edge between node 1 and 2 node 2 can only be adjacent to node 1 and node 1 can only be adjacent to node 2 and only once
        # Remove the tuple for node2 from node1's adjacency list
    for adjacent_node in graph_list[node1]: # iterate over the adjacent nodes of node1
        if adjacent_node[0] == node2: # if the adjacent nodes first element is node2
            graph_list[node1].remove(adjacent_node) # remove the edge between node1 and node2 from node1's adjacency list by removing the tuple (node2, weight)
            break  # Exit the loop once node 2 is found and is deleted from node1's adjacency list

    # Remove the tuple for node1 from node2's adjacency list
    for adjacent_node in graph_list[node2]: # iterate over the adjacent nodes of node2
        if adjacent_node[0] == node1: # if the adjacent nodes first element is node1
            graph_list[node2].remove(adjacent_node) # remove the edge between node1 and node2 from node2's adjacency list by removing the tuple
            break  # Exit the loop once the edge is removed


    