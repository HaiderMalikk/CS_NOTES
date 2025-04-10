# ! Trees in python
""" 
# ! a tree is a non linear data structure meaning unlike a list the next element dosent alwasy have to be left or right after another it can be anywhere but all the nodes must be connected
# ! there can also he a hierircy to trees meaning a node can have a parent and children nodes and a child node can have children nodes and so on.
# ! a tree is a recursive data structure meaning they can be divided into sub trees
# ! in a tree there can only be 1 path between 2 nodes, if there are more than 1 path then its a graph not a tree. this means 2 nodes cannot point to each other in a tree. only from one node to another.

### !!! NOTE: for the trees we build we only have a key and a leftchild and a rightchild but you can also have a value or data in the node
### !!!!!!!!! This would be useful if we wanted to build a heap tree using our definition of a node. the key (number) helps us order the nodes in the tree. the value is data that we want to store in the node.

A simple representation of a tree data structure.

Example Tree Structure:

               [Root]
              /      \
        [Child 1]    [Child 2]
        /       \             \
[Grandchild 1] [Grandchild 2] [Child 3]
    |
[Great Grandchild 1]

Tree Properties:
----------------
- **Node**: Each individual element of the tree. A node can contain a value and links to other nodes (its children). 

- **Edge**: An edge connects a parent node to a child node. In a tree, each edge represents a link that allows traversal between nodes basicaly a edge connects 2 nodes and is a path between them. NOTW: Number of edges = number of nodes - 1

- **Path**: A sequence of nodes in a tree that connects a two nodes. here the path between root and grandchild 2 is: [Root] → [Child 1] → [Grandchild 2]. NOTE: there are only one unique path between 2 nodes in a tree. 

- **Root**: The topmost node of the tree. There is only one root node in a tree. It serves as the entry point for traversal.

- **Leaf**: A node that does not have any children. In the above structure, `[Great Grandchild 2]` and `[Child 3]` are leaf nodes. NOTE: a non leaf node would be a parent node. also called external nodes, a internal node is a node that is not a leaf node.

- **Children**: The nodes that are directly connected to a given node when moving away from the root. For example, `[Child 1]` and `[Child 2]` are children of `[Root]`. NOTE: a child node can have only 1 parent 

- **Parent**: The node that has one or more children. For instance, `[Root]` is the parent of `[Child 1]` and `[Child 2]`. NOTE: a parent node can have multiple children. NOTE: each node must only have 1 parent (except root).

- **Sibling**: Nodes that share the same parent. `[Child 1]` and `[Child 2]` are siblings since they share the same parent `[Root]` notice how there on the same level.

- **Ancestor**: A node that lies on the path between the root and a given node. For example, `[Root]` is an ancestor of `[Great Grandchild 1]`. NOTE: the root is the ancestor of all nodes in the tree. for '[great grandchild 1]' the number of ancestors is 4 (root, child 1, grandchild 1, great grandchild 1) this is the ancestor path for '[great grandchild 1]'. this path for every node will be unique. any node is its own ancestor

- **Descendant**: A node that lies on the path between the root and a given node. For example, `[Great Grandchild 1]` is a descendant of `[Root]`. NOTE: all nodes in the tree are descendants of the root. for 'Child 1' the number of descendants is 5 (child 1, grandchild 1, great grandchild 1, grandchild 2, child 3) since there are many descendants we can take multiple paths as we have multiple descendants so the decentant path for 'Child 1' is not unique. any node is its own descendant

- **Neighbors**: In a graph, a neighbor node is any node that is directly connected by an edge. here child 1 is a  neighbor of root, GC1 and GC2

- **Subtree**: A tree consisting of a node and all its descendants. For example, the subtree rooted at `[Child 1]` includes `[Child 1]` (the subtrees new root), `[Grandchild 1]`, `[Grandchild 2]`, and `[Great Grandchild 1]`. NOTE: for the subtree at child 1 the grandchild 1 would acctualy be a child of child 1 if we were to traverse it. NOTE: every next node will have its own subtree or subtrees on left right etc. The smallest subtree is a leaf node and the largest subtree at the root. The Number of subtrees in a tree is equal to the number of nodes in the tree.

- **Height**: The height of a node in a tree is the number of edges in the longest path from the node to a leaf (known as the path). For example, the height of `[Root]` is 3 (from root to GGC1). the height of '[Child 1]' is 2 (from child 1 to GC1). Dont confuse with depth. Depth is from the root to the node height is from the node to the leaf node. NOTE: the height of a tree is the height of the root node.

- **Depth/Level**: The depth of a node is the number of edges from the root to that node (known as the path). The root node has a depth of 0, its children have a depth of 1, and so on. NOTE: the depth starts at 0 and the depth of the tree (max depth) is the length of the longest path from the root to a leaf, so the max depth of this tree is 3 (from root to GGC1) = to the number of edges in that path = depth of the tree, Dont confuse with height. Depth is from the root to the node height is from the node to the leaf NOTE: the depth of a tree is the depth of the leaf node. if a node has the same depth as another then they are one the same level

- **Degree of a node**: The degree of a node is the number of children it has. For example, the degree of `[Child 1]` is 2 (it has two children: `[Grandchild 1]` and `[Grandchild 2]`), while the degree of `[Child 2]` is 1 (it has one child: `[Child 3]`). 

- **Degree of a tree**: The degree of a tree is the maximum degree of any node in the tree or can be the max number of children that a particular node has. here root and child 1 have a degree of 2 while all others have 1 or 0 this means the degree of the tree is 2.

- **Orderd Tree**: A tree in which the nodes are ordered in a specific way. For example, a binary search tree is an ordered tree where the nodes are ordered in a specific way. our tree is ordered as the root is the first node and the children are ordered in a specific way (left to right) and so on.
"""

# ! Trees can have many types, but only one type of data structure, by type of trees we mean binary trees or n-ary trees etc what makes these trees different is that they have different properties meaning they have different shapes and structure and rules.
# ! here are some common tree structures and descriptions
"""
Tree Types Overview:

# Trees covered:
0. **General Tree**:
   - Definition: A tree in which each node can have any number of child nodes i.e there is no limit on the number of child nodes a node can have.
   - Characteristics:
     - any node can have any number of children.
     - the tree above given in the example is a general tree.
   - Uses: Various.

1. **Binary Tree**:
   - Definition: A tree in which each node has at most two children, referred to as the left child and the right child.
   - Characteristics: 
     - Each node can have 0, 1, or 2 children.
     - In a full binary tree, every node other than the leaves has exactly two children meaning any node can have 2 children or 0 children (making it a leaf). (a special case of a complete binary tree). Also called a proper binary tree.
     - In a complete binary tree, all levels of the tree except the last level are completely filled (meaning must have 2 child nodes). Last level can be either completely filled or filled left to right meaning that if the last level has 2 child nodes they must be on the left most node of the previous level. if we have one node it must be a left node to the left most node of the previous level. This left most node must be filled first before moving to the right
     - In a Perfect binary tree, all the nodes except for leaf nodes have 2 children and all the leaf nodes are at the same level.
     - In a Balanced binary tree, the difference in height between the left and right subtrees of every node is at most 1. This means at each node the left and right subtrees must be as close to the same height as possible.
     - In a pathalogical binary tree, every parent node has only 1 child node.
     - total number of nodes = num of nodes in left subtree + num of nodes in right subtree + 1. (+1 for the root node)
   - Uses: Commonly used in various applications such as expression trees for evaluating mathematical expressions and heaps for efficient data storage. Also used for decision trees in machine learning, binary search trees for efficient searching and sorting, and Huffman coding trees for data compression.

2. **Binary Search Tree (BST)**:
   - Definition: A special type of binary tree that maintains a sorted order of elements.
   - Characteristics:
     - The left subtree at every node contains only nodes with values less than the parent node.
     - The right subtree at every node contains only nodes with values greater than the parent node.
     - NOTE: if root is 50 , left subreet is 30 and right subtree is 70 then this is fine, BUT the node 30's left subtree must me less than 30 while its right node must be greater than 30 but less than 50 as 30 (its parent node) is on the left of node 50 (the node 30's parent node) hence all of the values below it the left must be less than 50. 
     - the left and right subtrees at every node must be a BST themselves.
     - Duplicate values are typically not allowed, or handled in a specific way (e.g., by allowing duplicates in the right subtree).
     - Given a list of values you can create a BST using the rules above inserting elements only when it dose not break the BST.
     - 2 Equal Node values: if 2 nodes in any level of the tree have the same value then; 1) it must be on the left side of the parent. 2) it must be on the right side of the parent 3) ignore duplicates. NOTE: (these are the most common cases and BST's duplicate rules may vary). Another approach is too use a counter to count the number of nodes that have the same value. and only update that nodes first occurance with that counter.
     - total number of nodes = #of nodes in left subtree + #of nodes in right subtree + 1. (+1 for the root node)
   - Uses: Efficient searching, insertion, and deletion of elements with an average time complexity of O(log n) when balanced; used in applications requiring sorted data, such as databases.

  - Operations: 
    - Search: Starting at root node we serch for our given value in our BST
      NOTE: we run the function below recursively until we find the value or run out of nodes at each node we check if this is out value if not we branch accordingly to the left or right subtree depeneding on given node (in else block) when our node is found we return it in line 2 if we run out of nodes we return not found in line 1 
      Recurtion: // we start at the root and search until found meaning recurtion
        if node == Null: return not found or Empty BST // if node is empty we are finished, after n branches we will branch again to a empty node (where no node exists) and this statement will return not found
        if node == given value: return node // if node is found return it 
        if given value < root node: search left subtree by branching to left child this will be the new node (root) // in BST values smaller than root are on the left
        if given value > root node: search right subtree by branching to right child this will be the new node (root) // in BST values greater than root are on the right
    
    - Insertion: To add a given node at the corrent position in a BST
      Recurtion: // start at rote node find a place to insert the given node
        if node == Null: insert element // if BST in empty we can instert the element at the root, When we treverse the tree (meaning function runs and BST not empty initially) and eventualy run out of nodes after n branches and we will branch to a empty node, we can insert the node here (this safe spot was found by line 3&4)
        if node == newnode: return // Duplicate value NOTE: duplicates instertion is subjective 
        if node < newnode: insert at right subtree so we will branch right and the right child will be the new node (new root) // if node is less than new node we branch to the right subtree as nodes smaller that current node (can be root) are on the right
        if node > newnode: insert at left subtree so we will branch left and the left child will be the new node (new root)// if node is greater than new node we branch to the left subtree as nodes greater that current node (can be root) are on the left

    - Deletion: To delete a given node in a BST
      NOTE: the deletion is not always at the end if its in middle we must link our tree back so it has no gaps from the deleted element: There are 3 cases
      - 1. node to be deleted is a leaf node (no children)
      - 2. node to be deleted has only 1 child
      - 3. node to be deleted has 2 children (max childern for BST)
      The deletion operation will depend on the 3 cases
      Recurtion: // start at root node and find the node to be deleted
        Searchfor(given node) // serch fofr node using serch operation
        if node == Null: return not found or Empty BST // if node is empty we are finished no node to delete, after n branches we will branch again to a empty node (where no node exists) and this statement will return not found
        if node == given node && has 0 Childen: delete node // if node is found and has no children delete it as we dont need to keep track of children before deletion there is nothing after it   
        if node == given node && has 1 Childen: node = node.child  // if node is found and has 1 child replace that node with its child (basicaly deleting that node) NOTE: the notes after node.child will be preserved meaning node.child.child will we node.child after this line runs
        if node == given node && has 2 Childen: node = node.largestvalueinleftsubtree || node = node.smallestvalueinrightsubtree // if node is found and has 2 children we have two options and they are self explanitory. we can choose any. 
        
        ~ // EX: lets say node 10 has leftnode(7) rightnode(12) if we replace node 10 with right node(12) the 7 will still be on the left side on newnode, we replaced 10 with 12 but 7 was on the left of 10 so it will be on the left of 12. This also works for choosing the left subtree as newnode.
             NOTE WE ASSUME THAT 7 & 12 have NO children
        ~ // EX NOTE: if the child nodes had mor child nodes we need to pick largestleftval or smallestrightval because all values after this new node have to follow BST lets say the node 7 had 8 as a child i need to replace 10 with 8 because 7 was on the left of 10 and it will be on the 
             left of 8 after replacing here the largest value in the left subtree dose satisfies BST if we chose 7 then the left subtree will have value > than parent which is not allowed in BST (NOTE: same logic for right subtree)

    - Treversal: To traverse a BST its not linear, we must visit each node once and in a specific order not linear (i.e first second third etc). There are different types of traversal for BST, different alogrithims visit nodes in different orders. here are some: NOTE(for the tree examples assume that the given tree is a BST in that smaller value on left and larger value on right for every node)
      - 1. Pre order Traversal (works on any Tree): Visit the root node, then the left subtree, then the right subtree. DO THIS RECURSIVELY! meaning the node on left and right subtree will become the new root node 
           and we will do steps 2 and 3 on both left and right nodes over and over Recursilvely until we run out of nodes meaning the node is a leaf node. NOTE: the step 1 is checking the root but here the root is the left or right subtree of the prevoius root. 
           so after printing this root which is on the left or right subtree we will do the same steps on the left node of this left node until  we run out of nodes on the left subtree then we go right and check for left children on this right node until we run out of left children on this right node then we go right on this right node and do the same steps until we have no left children on this right node we repete this until we run out of nodes
           EX: in the first ex tree after first run we will get in this order: (Root, Child1, G1, GG1, G2, C2, C3) at each root we alwasy fully traverse all the left nodes of each left nodes (ie the left subtree) when we run out of left nodes we go right this is our new root and we must first now cehc kif this root has a left serch the left like befrore if it dose then once we run out we go right. and so on until we are done with all the nodes.
      - 2. In order Traversal (works only on BT's): Traverse the left subtree, then the root node, then the right subtree. DO THIS RECURSIVLY! meaning after going to thr right node we must go to the left most node of this right node and so on until we run out of nodes meaning the node is a leaf node
           EX: in the first ex tree after first run we will get in this order: (GG1, G1, C1, GC2, Root, c2, c3) note how from the left most node we bo back up checking to see if we can go right after finishing the right subtree we go right back where we branched right and move back once more
           once we reach the root of bst we do the. NOTE!: by doing this traversal we will get the values in order smallest to largest. in order is a type of DFS for BT's
      - 3. Post order Traversal (works on any Tree): Traverse the left subtree (at first the left most node on left side of root), then the right subtree, then the root node. DO THIS RECURSIVELY at each node! just like before after this step the new root node will
           EX from tree: (GG1, G1, G2, C1, C3, C2, Root) note how we go to left most then backwards until we reach a node with right node and do the same first step of going as left as we can and repeting.
      - 4. Breadth First Traversal (works on any Tree): Traverse each level of the tree from left to right then move onto the next level do this from top to bottom (level 0 to level n). DO THIS RECURSIVELY! EX from tree: 1) root, 2) Child one and child two 3) GC 1 and GC2 and Child 3 and so on. going level by level in each level left to right. NOTE: this is the only traversal that is linear. 
      - 5. Depth First Traversal (works on any Tree): Traverse the tree in a depth first manner. meaning starting a the root visit any neigbour node and keep doing deaper traversing each neighbours neighbours until you reach a node with no unvisited neighbors (leaf), backtrack to the last node with unvisited neighbors. Repeat until all nodes are visited. EX: root, Child, G1, GG1, G2, Child 2, Child3
      - Note (traversal for General Tree): in the case of a GT where a root has say 3 children if we use pre order we would do root then the left most child then the middle child then the right child. this follows the root left right, as wee visit the root tehn make our way left to right on the children. if say the left child had 2 children we would visit that left child then goto its left child then right child then goto the middle child then teh right child. this follows for all (pre order, in order, post order)

    NOTE!: When i say left node right etc, i mean from the root(first node) we go left until we cant go left anymore meaning no left node exits only then can we move on to the next step in this case we goto node
    node is just the current node (we can print this node etc), after this node we can goto the right of this root (as no more left nodes) and right after this we repeat meaning we check for left nodes again on this right node until no more left nodes then we goto root then right so on
    until none of the condtions are met meaning on the last node we will have no left or right node to go to. NOTE: when we reach a node with no childen we go backwards meaning we go to the last node we visited before we branched. once we reach a point where we have no left or right node to go to we go back to the last node we visited before we branched we end.
    in the code you will se this as recurtion we keep going deeper and as one recusive call finsihes we go to the prevoius one ie the call than called this call we just finished and once we reach the first call thats when we go back to the first node we branched at (meanign the caller of the first recursive call) and we end.

    - Min and Max values (nodes): (Given a Non Empty BST) The min value is the smallest value in the BST and will be in the left subtree. The max value is the largest value in the BST  and will be in the right subtree. IF no left node or IF no right node then root is the smaller or larger value respectively.
      since each time a new node is made the smaller child is on the left this means the smallest value will be on the left most node of the tree. same logic for max value it will be on the right most node. EX: in the first ex tree assuming its a BST like we said: Min = GG1, Max = Child 3
      to find it manually we would treverse the trees left and right subtrees and find the smallest and largest value by traversing untill no left or right node exits the nwe will know that our currrent node is a minimum or maximum node respectfully.

8. **Binary Heap Tree**: (NOTE there are more types of heap trees)
   - Definition: A complete binary tree that satisfies the heap property, where each node has a specific order relative to its children.
   - Heap is Used for dynamic memory allocation, can grow and shrink in size during program execution.
   - Heap property => for any given node, the parent node is either greater than (max heap) or less than (min heap) the children node, so if every node is greater than or equal to its children its max heap or if its less than or equal to its children its min heap and the tree must be a complete binary tree.
   - NOTE: for a heap tree to be a valid heap tree it must be a complete binary tree and the heap property must be true for all nodes in the tree. a complete binary tree is a tree where all levels are completely filled except for the last level, which is filled from left to right. this means that the last level can be partially filled but must be filled from left to right.
    - Characteristics:
      - **Max-Heap**: The value of each node is greater than or equal to the values of its children. the root node is the max value.
      - **Min-Heap**: The value of each node is less than or equal to the values of its children. the root node is the min value.
      - Implemented as an array, where parent-child relationships are defined by indices. 
    - Uses:
      - Efficiently implements priority queues, enabling quick access to the highest or lowest priority elements.
      - Forms the basis for the heapsort algorithm, sorting elements in O(n log n) time.
      - Utilized in graph algorithms, such as Dijkstra's algorithm, for efficient minimum element retrieval. and kth largest element.
      - Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure.
      

# other trees not covered:
3. **Balanced Binary Search Tree (BBST)**:
   - Definition: a balanced binary search tree combines the properties of a binary search tree and a balanced binary tree. a BBST is balaned as every node's left and right subtrees differ in height by at most 1. and is a search tree meaning that for every node, all elements in the left subtree are less than the node and all elements in the right subtree are greater than the node.

4. **Balanced Trees**:
   - Definition: Trees that automatically keep their height minimal, such as AVL trees and Red-Black trees.
   - Characteristics:
     - Height balancing ensures efficient operations like search, insert, and delete (O(log n)).
     - AVL trees maintain a strict balance factor, while Red-Black trees use color properties to ensure balance.
   - Uses: Often used in database indexing, memory management systems, and applications requiring frequent insertions and deletions.

5. **N-ary Tree**:
   - Definition: A tree in which each node can have at most N children.
   - Characteristics:
     - More flexible than binary trees, allowing multiple children, which can vary from node to node.
     - Useful for representing hierarchical data where a node can have an arbitrary number of children.
   - Uses: Suitable for representing hierarchical structures, such as file systems, organizational charts, and XML/JSON data representation.

6. **Trie (Prefix Tree)**:
   - Definition: A tree used for storing a dynamic set of strings where the keys are usually strings.
   - Characteristics:
     - Nodes represent prefixes of keys, allowing fast retrieval of strings based on common prefixes.
     - Each edge represents a character, and each path from the root to a leaf node represents a complete string.
   - Uses: Useful in applications like autocomplete features, spell checkers, and IP routing, where fast retrieval based on prefixes is necessary.

7. **Segment Tree**:
   - Definition: A tree used for storing intervals or segments, allowing efficient querying of overlapping segments.
   - Characteristics:
     - Each node represents a segment, and leaf nodes represent individual elements.
     - Allows querying which segments overlap with a given point efficiently, typically in O(log n) time.
   - Uses: Commonly used in computational geometry for finding range queries, updates, and interval problems, such as calculating the sum of elements over a given range.

8. **B-Tree**:
   - Definition: A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
   - Characteristics:
     - Nodes can have multiple children (more than two), and all leaves are at the same level.
     - It is designed to work well on disk and can handle large amounts of data efficiently, minimizing disk reads.
   - Uses: Used in databases and file systems for efficient data retrieval, ensuring that operations remain efficient even with large datasets.
"""

# ! IMPLEMENTING TREES IN PYTHON CODE

# ! Bianary Search Tree Implementation in python (for more detail refer to the topic aboove where BST are explained in full detail)
# a tree is a selection of nodes, each node has 3 parts: key(data) left child and right child. We will use class and object to create a tree
# each node is a object and it will have 3 properties: key, left child and right child
""" 
# EX of a BST diagram:

     10
    /  \
   5   20
       / \
     15  100
     
- DEF: every node in the left subtree of a parent node must be less than the parent node and every node in the right subtree must be greater than the parent node and every node itself must be a BST.
     
NOTE: 
       x
      / \
    15  100
    \
    120
  
THIS IS NOT VALID BECAUSE 120 IS NOT A CHILD OF 100, even though 15's left child is 120 > 15 its also greater then an node which in the BST which is not its parent (100) so this is not a valid BST.
Another way to think about it is that every node in the left subtree of 20 must be less than 20 and every node in the right subtree must be greater than 20 (as 20 is the parent node).
This is so when we are serching for ex 120 we would branch right on 20 and go right as 120 > 20 but is 120 is on the left side it will never be found hence its unvalid
      

# in the repersentation below we can see what the tree above would look like in actual memory. each square is a node with key(data) left child and right child (the references to them) 
# once we get to the left child or right child we then have accsess to data and there children and the proccess is repeated until we reach a leaf node (recursively done).
# you can think of the edges (the path to the next node) as a pointer. with the reference we can go to the next node this reference is the path (simmilar to linked list).

# A repesentation of a BST in memory:
# NOTE: the ref is a random number repeseting the address of the object in memory for the sake of simplicity this address would give us the object so then we could access the data and the children
                         ____________
                        |  ref: 5000 |
                        |  value: 10 |
                        |------------|
                        | Left: 5100 |
                        | Right: 2100|
                        |____________|
                               |
                 ______________|________________
                |                               |
                |                               |
         _____________                     ____________
        |  ref: 5100  |                   | ref: 2100  |
        |  value: 5   |                   | value: 20  |
        |-------------|                   |------------|
        | Left: null  |                   | Left: 7900 |
        | Right: null |                   | Right: 3200|
        |_____________|                   |____________|
                                               |
                               ________________|____________________
                              |                                     |
                              |                                     |
                       _____________                        _____________
                      |  ref: 7900  |                      |  ref: 3200  |
                      |  value: 15  |                      |  value: 100 |
                      |-------------|                      |-------------|
                      | Left: null  |                      | Left: null  |
                      | Right: null |                      | Right: null |
                      |_____________|                      |_____________|


"""

# ! BST code

# here like linked list we can have 2 classes (one for node and one for LL) but here we will have just one class for BST and no class for the node in our BST
# ! creating the binary search tree
class BST: # create class
    # create constructor, constructor makes teh object(in our case the node) our node has 3 properties: key, left child and right child, self repersents the object here the current node 
    # but when we create the node we only need to give the key as initially the node has no children and  we can define the variables for them and fill them when we creat the left or right node 
    # now when we create the node object we only need to give the key and the rest will be filled automatically by the otehr methods when we difine the left or right child
    def __init__(self, key): 
        self.key = key
        self.leftchild = None
        self.rightchild = None
    
# using this lets create the Ex bst above:
"""
     10
    /  \
   5   20
       / \
     15  100 
"""

# ! create a BST object and adding nodes
root = BST(10) # here we create a node and give it a key this has a left and right child but they are None this is our first node (root)
print(root.key)  # print the key of the root node which is 10
print(root.leftchild)   # print the left child of the root node which is None right now
print(root.rightchild)   # print the right child of the root node which is None right now

# assigning the left child and right child to the root
root.leftchild = BST(5)  # here we create a new node object with a key of 5 and assign it to the left child of our root. but rememeber in creating node we also give the left and right child variables that can be added (currently none). this means this child node can have 2 more children and so on.
root.rightchild = BST(20) # here we create a new node object with a key of 20 and assign it to the right child of our root. this right child node can also have 2 more children and so on.
print(root.leftchild.key)   # print the key of the left child of the root which is 5
print(root.rightchild.key)   # print the key of the right child of the root which is 20

# creating the roots right grandchild or the right childs right child
root.rightchild.rightchild = BST(100) # just like mentioned above the right child node is made with BST class so it too has left and right child variables that can be assigned here we assign the right child of root with its own right child with a key of 100. so node 100 is rigth child of rightchild or right grandchild of root
print(root.rightchild.rightchild.key)   # print the key of the left grandchild of root which is 2
# creating the right childs left child or the roots left grandchild
root.leftchild.leftchild = BST(15) # here we assign the left child of the
print(root.leftchild.leftchild.key)   # print the key of the left grandchild of root which is 15

# now our bst is completed, see the memory digram above to see how the tree looks like in memory at this moment note the ref is a random number repeseting the address of the object in memory 
#so whe we make a new BST objec it gets a new ref for accsessing the object and its properties by doing root.leftchild we can assign the ref of the left child of the root so now when we print root.leftchild.key the computer have the ref of the left child and can access its key property and print it

# ! Insertion (this allows us to add new nodes to the tree) see notes above for details on this operation
# first check if inserting to empty BST then the new node is the root
# if not empty (has 1 or mpore node) we need to find the position of the new node. rmemeber the BST rules : all nodes to the left of a node have keys less than the node and all nodes to the right of a node have keys greater than the node so we would need to find a place for this new node that follows this rule
# but we only have 2 options at everynode we can go left or right so we just nee to find if we need to add the tree to the left or right subtree at everynode once we reach a leaf node we add it to its right or left child depending on if its greater or less than this leaf node.
# duplicate values are not allowed but we can handle duplicates in a specific way (e.g., by allowing duplicates in the right subtree). see notes above for details on this operation

# lets create out bst and then add the function to instert a new node
class BST: 
    def __init__(self, key): 
        self.key = key
        self.leftchild = None
        self.rightchild = None  
      
    # * Note: since i use if elif else the elif ie the search part only happens if the 'if' fails i.e self.key is not none if i used all 'if' statements they would all run regardless of if the 'if' fails before it to avoid that just add a 'return' after the 'if' statement. HERE I DO BOTH BUT ONLY ONE METHOD IS NEEDED 'if, elif, else' or 'if and return'
    # * ALSO since we have 2 elifs the second elif only happens if the first elif fails BUT i use a return statemnt to indicate that we break out of the function call and stop the insertion process
    def insert(self, data): # create insertion method with data as input
        if self.key is None: # if root is empty ie key is nune note, key is the value of node. if there is no value meaning no key then there is no root node. EX: say we make BST(None) and call BST.insert(10) since at the moment of calling insert, the key of our BST is None, hence we have no root node. so we assign the BST obejcts key (its value) by using 'self.key' with data of 10. now the BST object has a key of 10 this the root node. 
          self.key = data  # if there is no root node then we assign the nodes key with the value of data. NOTE: we dont create a new node we just check if its null if it is then we assign the key to data. NOTE: this must the root as we cannot have empty nodes in the middle of the tree initially the key can be null and that will become teh root node once we assign it a value. 
          return # we stop the insertion process here as we have created the root node and are done with the insertion
        elif self.key == data: # if the key of the root node is equal to the value of the new node then we have a duplicate key and we cannot add it to the tree
          print("Error: duplicate key") # print an error message
          return # stop the insertion process here as we cannot add a duplicate key to the tree
        # if tree not empty and we dont have a duplicate key, check if the node is greater or less than the current node so we know wether to go to the left or right subtree
        # note that key is the value of our root note as we traverse the tree this root changes and we check if its greater or less than the current node recursively.
        elif self.key > data: # goto left subtree as value of new node is less than current node 
          # here we must check if the left subtree is empty then we can dd the new node here. if its not emoty after travering some times we will reach the left subtree again and again untill we find a leaf nod at this leaf node the left child will be none and we can add the new node here
          if self.leftchild: # leftchild can be true or false but the condition only runs if its true that means we do have a left child
            # since we have a left child we must take the current node 'leftchild' as our new root node and do a insert again with the same value by calling the insert method on this leftnode (making it our root). 
            # when this function runs again and again at some point we will reach a leaf node then since we do still have a key(value) so if the comparison key > data is true (meaing we are still adding to left subtree) we will check if leftsubtree again but since the last root node we called insert on is a leaf node and its left child is none so now we can add the new node in the else block
            self.leftchild.insert(data)
          else:
            # since we have reached a leaf node the leftchild of this leaf node is none hand we can add the node here
            self.leftchild = BST(data) # create the new node with the value of data and assign it to the left child of the current node which before this was none
            
        # the code to add to right subtree is the same as the code to add to left subtree but we just need to change leftchild to rightchild
        else: # goto right subtree as value of new node is greater than current node
          if self.rightchild: # if we have a right child
            self.rightchild.insert(data) # call the insert method again on this right child node
          else: # at some point we will call the instert above on a leaf node and the right child of that node we called instert on is null and this part runs
            self.rightchild = BST(data) # since we have no right child here, we can add the new node here safely  
            
    # * dealing with duplicates
    # 1) we can add the follwing beofre branching: if key == data: return with this we do not add the node to the tree if the key is the same as the data we are trying to
    # 2) we can change our branch condition to key <= data or key >= data to include duplicates in our tree with this the duplicates will be added to either the left or right subtree.
          
    # * Summary: 
    # we compare value with data and brach left or right depending on the comparison. after the branch if we have a root node and depending on what subtree we branched to we call the insert method on the left or right child. 
    # once we reach a point where we have a leaf node we still have a key so we call insert again but this time after branching the left or right child will be null and we create the new node with data and it gets added to the left or right child of the leaf node.
    
# lets build the tree again with insert only
"""
     10
    /  \
   5   20
       / \
     15  100 
"""
# ! inserting automatically to tree using a list and loop
BSTnodes = [10, 5, 20, 15, 100]
root = BST(None)
for node in BSTnodes:
  root.insert(node)

# insetring manually to the tree
# create BST object
# root = BST(None)
# root.insert(10) # add 10 to the root node as so far the root node is empty
# root.insert(5) # add 5 to the left subtree of the root node
# root.insert(20) # add 20 to the right subtree of the root node
# root.insert(15) # add 15 to the left subtree of the right subtree of the root
# root.insert(100) # add 100 to the right subtree of the right subtree of the root

# uncoment to see output
# print(root.key) # prints 10
# print(root.leftchild.key) # prints 5
# print(root.rightchild.key) # prints 20
# print(root.rightchild.leftchild.key) # prints 15
# print(root.rightchild.rightchild.key) # prints 100
# all the nodes are printed all nodes after will have value of NONE

# ! Search (we can add nodes like we did at the very starts but since we know the insert operation lets use it and build on what we have so far)
class BST:
  def __init__(self, data):
    self.key = data
    self.leftchild = None
    self.rightchild = None

  def insert(self, data):
    if self.key is None:
      self.key = data
    elif self.key == data:
      return
    elif self.key > data:
      if self.leftchild:
        self.leftchild.insert(data)
      else:
        self.leftchild = BST(data)
    else:
      if self.rightchild:
        self.rightchild.insert(data)
      else:
        self.rightchild = BST(data)

  # * Search function (same idea as insert but insted of inserting we just check the current node = data if not we go left or right depending on data. at the end (leaf) or if theres no root insted of insterting a node we just return not found )
  def search(self, data):
    if self.key == data: # if the current node is the data we return found
      print("Node Found")  # print this message and return
      return
    
    if data < self.key: # if data is less than the current node we go left as the data is present of the left side of teh current root node
      if self.leftchild: # if left child is not null we call the serch operation of that leftchild. this serch runs with our leftchild as the new root and at the start of serch we check if current node is the data if its not we will branch again depending on the data if theres no leftchild we return not found
          self.leftchild.search(data) # if there is a leftchild search that left child. the serch function runs on LC as new root and 1) leftchild will be checked 2) if not = data we will branch again
      else:  # if there is no left child we return not found. NOTE: at some point we will reach a leaf and we will call the serch on this leaf node and this leaf will have no left child (same logic for right child) and we will return not found
        print("Node Not found")
        return
    
    # same as left subtree but for right subtree
    else: # if data is greater than the current node we go right
      if self.rightchild: # if right child is not null we call the serch operation of that rightchild
          self.rightchild.search(data) # there is a rightchild so we search that right child this will first check if RC = data is not we move forward in teh serch function and bracnch again 
      else:  # if there is no right child we return not found
        print("Node Not found")  # print this message and return
        return #  return from the serch function we are done
    
# Lets build this tree
"""
     10
    /  \
   5   20
       / \
     15  100 
"""
root = BST(None) # creating empty tree
# insterting all our nodes
root.insert(10)
root.insert(5)
root.insert(20)
root.insert(15)
root.insert(100)

# now lets serch
root.search(15) # this will print Node 15 Found
root.search(33) # this will print Node not Found

# ! Traversals (traversal meaning to visit each node once and here its in a specific, then we we can do things like print each node) we leaned 3 types:
# *  pre order traversal is root -> left -> right
# *  in order traversal is left -> root -> right
# *  post order traversal is left -> right -> root
# NOTE: the traversal is called on a node, and it can be called on any node, the node its called on will be the root of the traversal
class BST:
  def __init__(self, data):
    self.key = data
    self.leftchild = None
    self.rightchild = None

  def insert(self, data):
    if self.key is None:
      self.key = data
    elif self.key == data:
      return
    elif self.key > data:
      if self.leftchild:
        self.leftchild.insert(data)
      else:
        self.leftchild = BST(data)
    else:
      if self.rightchild:
        self.rightchild.insert(data)
      else:
        self.rightchild = BST(data)
        
  def preorder(self): # this is pre order traversal root -> left -> right
    print(self.key) # print the root (as key the value initially is the root, after ot can be any node)
    # now goto left subtree but check is it exist or not(as at some point the code needs to reach a leaf node (a node with no childern left or right) and stop)
    # the if's make sure we call the function on both the left and right child and we call left first and then right
    if self.leftchild:
        self.leftchild.preorder() # recurively call the preorder function on the left subtree this makes the left subree's left child a root(as we just called preorder on the left child) and then we go root -> left -> right again 
    if self.rightchild:    
        self.rightchild.preorder() # recurively call the preorder function on the right subtree this makes the right subree's right child a root(as we just called preorder on the right child) and then we go root -> left -> right again 
  
    # NOTE: 
    # 1) here we call the function recursively on a node, left or right of the root, but after calling that fucntion on a node that node becomes the root of the traversal and we repeat this untill we reach a root and we no longer have a left or right child
    # 2) Here we have 2 if's no elif or else this is because we want to call the function on both the left and right child if they exist, if they dont exist we just return and dont do anything. but we need to traverse both the left and right subtree hence we use 2 'if' blocks making sure both blocks run.
    # How it works: once we branch at the root we keep branching left first everytime until we have no left nodes left then the recurtion stops and we return back and finish the conditional now left child is none but if we have a right child we now serch the right child but if this right child has a left child we go left ..... come back branch again untill no left or right nodes exist. 

  def inorder(self): # this is in order traversal left -> root -> right
    if self.leftchild:
      self.leftchild.inorder() # recurively call the inorder function on the left subtree this makes
      
    print(self.key) # print the root this wont run until left child is none meaning we are at the left most node
    
    if self.rightchild: # once we reach the left most node we check if right child exists as we need to traverse the right subtree after left and root
      self.rightchild.inorder() # recurively call the inorder function on the right subtree this means we branch right and must now go all the way left again before printing root and then checking for right child again

  def postorder(self): # this is post order traversal left -> right -> root
    if self.leftchild: # if we have a left child
      self.leftchild.postorder() # recurively call the postorder function on the left subtree this makes
      
    # now we are all the way left just like before but we do not print the root (left most node like in inorder)
    # what we do is check if we can go right first, we will then repete teh whole function on this right node so we will go as left as we can on right node and so on until we have no left or right nodes left
    # then we print the curretn node (root) and as we return back to the function call one by one, we will print all nodes going left and then right and then root (current node)
    
    if self.rightchild: # once we reach the left most node we check if right child exists as we need to traverse the right subtree after left and root
      self.rightchild.postorder() # recurively call the postorder function on the right subtree this
      
    print(self.key) # print the root this wont run until left and right child is none (root is just the current node we are on its value is 'key')
    

# Lets build this tree and traverse it 
"""
     10
    /  \
   5   20
       / \
     15  100 
"""
root = BST(None) # creating empty tree
# insterting all our nodes
root.insert(10)
root.insert(5)
root.insert(20)
root.insert(15)
root.insert(100)

# now lets traverse
# Pre order traversal
root.preorder() # prints 10 5 20 15 100 None(before we branch we print root but root at the end is none so it prints none)
# In order traversal
root.inorder()  # prints 5 10 15 20 100 None (note its in lowest to highest order)
# Post order traversal
root.postorder() # prints 5 15 100 20 10 None 

# * DFS (Depth First Search) and BFS (Breadth First Search) also known as level order traversal 
class BST:
    def __init__(self, data):
        self.key = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
        elif self.key == data:
            return  # If the node already exists, we don't insert it.
        elif self.key > data:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild = BST(data)
        else:
            if self.rightchild:
                self.rightchild.insert(data)
            else:
                self.rightchild = BST(data)

    def bfs(self):
        """
        Performs a breadth-first search (BFS) on the binary tree and prints each node in level order.
        BFS uses a queue to explore all nodes level by level. hence its also known as level order traversal
        """
        # Start with the root node in the queue
        queue = [self]
        while queue:
            # Pop the first node in the queue (level-order traversal)
            current = queue.pop(0)
            print(current.key, end=" ")  # Print the current node's key
            # If the current node has a left child, add it to the queue
            if current.leftchild:
                queue.append(current.leftchild)
            # If the current node has a right child, add it to the queue
            if current.rightchild:
                queue.append(current.rightchild)

    def dfs(self):
        """
        Performs a depth-first search (DFS) on the binary tree and prints each node.
        DFS explores as far down as possible along each branch before backtracking.
        This DFS implementation uses in-order traversal, meaning it visits the left child, 
        then the current node, and then the right child. it will goto the leftmost node and then go right and then back to root
        """
        # Traverse the left subtree first
        if self.leftchild:
            self.leftchild.dfs()
        # Print the current node's key
        print(self.key, end=" ")
        # Traverse the right subtree
        if self.rightchild:
            self.rightchild.dfs()


# Example of usage:
""" 
    10
   /  \
  5    20
      /  \
     15  100
"""
# Create a binary search tree
root = BST(10)
root.insert(5)
root.insert(20)
root.insert(15)
root.insert(100)

print("Breadth-First Search (BFS):")
root.bfs()  # Expected Output: 10 5 20 15 100 (level-order)

print("Depth-First Search (DFS):")
root.dfs()  # Expected Output: 5 10 15 20 100 (in-order)

# DFS vs inorder
""" 
DFS (Depth-First Search) is a general traversal strategy that explores as deeply as possible along each branch before backtracking, 
while **in-order traversal** is a specific type of DFS used in binary trees. In-order traversal visits nodes in a left-root-right order, 
making it particularly useful for Binary Search Trees (BSTs) to retrieve nodes in sorted order. While DFS refers to the overall approach, 
in-order is a specific implementation of DFS focused on a particular sequence of node visits in binary trees.

so in short: DFS goes as deep as possible and can be used in any tree, in-order traversal is a specific DFS used in BSTs and BT's
used to retrieve nodes in sorted order, inorder also goes as deep as possible because of the way a BST is structured
since inorder finds the smallest node first it has to go as deep as possible to find the smallest node.
"""

# ! Deleting a node from a tree including root node, or if root has 1,2 children, see counter for deleting leaf root node
""" 
procedure:
1) check if tree is empty: if yes then return and either tree is empty or we ran out of nodes to delete and key is null
2) if not empty find the node to be deleted (using custom search not serch method)
3) if the node is found then delete it 
"""
class BST:
  def __init__(self, data):
    self.key = data
    self.leftchild = None
    self.rightchild = None

  def insert(self, data):
    if self.key is None:
      self.key = data
    elif self.key == data:
      return
    elif self.key > data:
      if self.leftchild:
        self.leftchild.insert(data)
      else:
        self.leftchild = BST(data)
    else:
      if self.rightchild:
        self.rightchild.insert(data)
      else:
        self.rightchild = BST(data)
      
        
  def delete(self, data, current): # one arg is data (for serching) and current is the current node (for deleting) (used for node so you must give the root)
    if self.key is None:  # if tree is empty or when we ran out of nodes to delete and key is null, NOTE: self is teh current node
      print("Tree is empty")
      return # return as we are done with the function 
    
    # to find a note recall it can be on left or right (data is less than or greater than key) or data is equal to key
    if data < self.key: # if data is less than key we go left
      if self.leftchild: # if left child exists we call the delete function on that left child as the node we are deleting might be in the left subtree
         # call the delete function on the left child until we find node or we ran out of nodes to delete, this along with the recusive call in right branch "elif" will run until we have no left or right child left
        self.leftchild = self.leftchild.delete(data, current) # here we store the result given by the delete function (found or not) in left child beacuse we are deleting a node from the left subtree, current mus talso be given as that was given at teh fuction call
      else: # if left child does not exist but the data we are looking for is less than key then we return None as we ran out of nodes to delete the node has to be on left and it is not so node we want to delete DNE
        print("Node not found")
    elif data > self.key: # if data is greater than key we go right
      if self.rightchild: # if right child exists we call the delete function on that right child as the node we are deleting might be in the right subtree
        self.rightchild = self.rightchild.delete(data, current) # call the delete function on the right child until we find node or we ran out of nodes
      else: # if right child does not exist but the data we are looking for is greater than
        print("Node not found")
        
    else: # if data is equal to key than the node we are deleting in the root node ie our current node is the node we want to delete
      # * here we have three cases: 1) no child then just delete, 2) one child then that child will replace the parent, 3) two child then replace the gretest value in the left subtree or smallest value in the right subtree with the parent, one child then that child will replace the parent with that child
      # * IF WE WANT TO DELETE ROOT THIS ONLY WORKS IF ROOT HAS 1 or 2 CHILDREN 
      # * NOTE: all nodes are deleted regardless of the number of children. the case of having 1 or 2 children is only for root node (initial node of BST)
      # case 1 and 2 combined (covers case of 1 child as 1 child means wither left or right child noe both)
      if self.leftchild is None: # if there is no left child then we delete the current node and replace it with its right child, i choose the right child as it is the only child
        temp = self.rightchild # store the right child in a temp variable (as we will soon delete its parent and lose accsess to it), if RC is none that ignore and LC and Rc are none its a leaf and condition 1 applies
        # if root node has 1 node and left child is none
        if data == current: # deleting root node with one child by replace it with the right child
          self.key = temp.key # curretn node to delete = curretn nodes rigth child
          self.leftchild = temp.leftchild # current nodes left child = current nodes right child's left child
          self.rightchild = temp.rightchild # current nodes right child = current nodes right child's right child
          temp = None
          return 
        self = None  # delete the current node
        return temp  # return the right child as we have deleted the current node now we return this and it will get stored in the lef tor rigth child of the parent of the current node (as that parent called the detetion on its left or right child) EX: see the line where we do LC = LC.delete(data) to get here that LC's LC would be nome and hence we would change LC's LC to the right child by returning the LC = temp (temp = RC) now LC is the LC's RC NOTE: its the same logic for RC = RC.delete(data)
        # NOTE: we use temp because we need to store the child before deleteing its parent (current node) as we will lose access to it after deletion we still have all of rightchilds children but to get to right child and its children we had to use the parent which is why we has to keep the link to rightchild using temp and returning it so we can essentially fill in the deleted nodes gap
      if self.rightchild is None: # if there is no right child then we delete the current node and replace it with its left child, i choose the left child as it is the only child
        temp = self.leftchild  # store the left child in a temp variable 
        # * if root node has 1 node and right child is none
        if data == current: # deleting root node with one child by replace it with the left child
          self.key = temp.key # curretn node to delete = curretn nodes left child
          self.leftchild = temp.leftchild # current nodes left child = current nodes left child's left child
          self.rightchild = temp.rightchild # current nodes right child = current nodes left child's right
          temp = None
          return
        self = None # delete the current node
        return temp # return the LC
      # case 3 2 children as past two if blocks did not run NOTE: i choose option 2 replace the parent with the smallest value in the right subtree
      # to find the largest or smallest we use a while loop
      node = self.rightchild # start at the right child
      while node.leftchild:  # while the right child has a left child we keep going left as we want the smallest value of teh right subtree which is the leftmost node
        node = node.leftchild # keep going left now the node is the left child and we run the loop again this time we go left again nso we goto the LC's LC we do this until we find the leftmost node where LC is none
      # so far either we have the smallest value the leftmost node or if there was no left node of this parent node the curret node (right child) is the smallest value, so if theres no Lc than the left most node is the current node = RC
      # Note that the last two if blocks failing means we have 2 children but we took node as RC so whe nwe did while node.RC we we said while RC.LC esentially cehcking the left child of this RC node which is one of two nodes of the node we are deleting 
      self.key = node.key # set the key of the current node to the key of the leftmost node (which is the smallest value) so basically we say key(value of current node we called method on) = node.key( the smallest value in the right subtree the 'selfs' RC's smallest value) We basiclly insted of deleting the node we cahnge its value to the smallest value in the right subtree which is the leftmost node esantially deleting the node we want to delete by replacing its value
      self.rightchild = self.rightchild.delete(node.key, current) # from the prevoius line we took the node we were deleting and gave it the value of its right childs smalest value (its RC's leftmost node) now that the node we were deleting is updated with what we wanted we need to delete the 'node' which was the leftmost node of the right subtree but since we set that to our current node to be deleted 'self' we essentialy deleted that node by replacing it with 'node' but now 'node' is a duplicate and must be deleted

    return self #  return the current node as we are done with the function and we want to return the current node to the parent of the current node (as the parent called the delete function on its left or right child) now self is replaced with the node we wanted (the node to delete's RC's leftmost node ie the smallest value in the RC) for ex the LC = LC.delete(data) will get LC = self (self is the node to delete's right childs leftmost node ie RC's smallest value) by retrning this we esentially update the node we needed to delete basiacly removing it from the tree
  
# ! DELETION for deleting the root node from BST (also has 3 cases) we only did the case of root having 2 children this is a helper method for case 1,2,3
# 1 if root node is leaf node, 2) if root node has 1 child, 3) if root node has 2 children
# the last method only works if root has 2 children CASE 3, lets make the method work for the other two cases
# 1) if root is leaf than BST has 1 node ! we cannot delete this as its a leaf root node, 
# We must count the number of nodes first before we do this using helper function
def count(node): # counting number of nodes in the tree
  if node is None:
    return 0
  # to count nodes do root + nodes in left subtree + right subtree
  return 1 + count(node.leftchild) + count(node.rightchild) # by using recution we cover all the nodes by counting each node (1) + its left node + its right node, this line runs for each node in the tree recursively going deeper in the tree if no RC or LC we return zer o as node will we none

# * when deleting you must give the root node as a parameter to the deletion method for it delete wrap in if else to check if # of children is 0 using count function if zero then cant delete root
# * case 1 lets delete a root node that is a leaf I.e a BST with 1 node itslef
root = BST(10)
if count(root) > 1: # counts nodes including root so for this to run BST # of nodes must be more that 1 so root plus at least 1 other node (child)
  root.delete(10, root.key)
else:
  print("cannot delete root node with less than 1 nodes") # will run as root is leaf 
  
#  * case 2 lets delete a root node that has 1 child
root = BST(10)
root.leftchild = BST(5)
root.rightchild = None
if count(root) > 1: # counts nodes including root so for this to run BST #
  root.delete(10, root.key)
else:
  print("cannot delete root node with less than 1 nodes") # will run as root is
# NODE 10 is deleted and new BST is '5' with no children

# * case 3 lets delete a root node that has 2 children
# Lets build this tree and delete values from it # works for case 3 if root has 2 children
"""
     10
    /  \
   5   20
       / \
     15  100 
"""
root = BST(None) # creating empty tree
# insterting all our nodes
root.insert(10)
root.insert(5)
root.insert(20)
root.insert(15)
root.insert(100)
root.delete(100, root.key) # not root
# new tree
"""
     10
    /  \
   5   20
       /
     15   
"""
# deleting root here root has 2 childs so we can delete
if count(root) > 1: # counts nodes including root so for this to run BST #
  root.delete(10, root.key)
else:
  print("cannot delete root node with less than 1 nodes")
# printing all nodes in the tree manually 
print(root.key)
print(root.rightchild.key)
print(root.leftchild.key)
# new tree note when root has 2 children we choose smallest val in rigth subtree
"""
     15
    /  \
   5   20  
"""

# ! Min and Max of BST
# NOTE: we dod not have to serch the whole tree and find the max its a BST the smaller value will be in the left subtree and the larger value will be in the right subtree
# so the smallest vlaue (MIN) is at the left most node and the largest value (MAX) is at the rightmost node
# So until we have no left node or no right node then the current node is the smaller or larger value respectively
class BST:
  def __init__(self, data):
    self.key = data
    self.leftchild = None
    self.rightchild = None

  def insert(self, data):
    if self.key is None:
      self.key = data
    elif self.key == data:
      return
    elif self.key > data:
      if self.leftchild:
        self.leftchild.insert(data)
      else:
        self.leftchild = BST(data)
    else:
      if self.rightchild:
        self.rightchild.insert(data)
      else:
        self.rightchild = BST(data)
  
  def min_node(self):
    if self.leftchild: # if we have a left child then we go to the left child
      return self.leftchild.min_node() # serch the left subtree for minimum this will keep running until we reach a node with no left child
    return self.key # once we reach a node with no left child then this node is the minimum value

  def max_node(self):
    if self.rightchild: # if we have a right child then we go to the right child
      return self.rightchild.max_node() # serch the right subtree for maximum this will keep running until we reach a node with no right
    return self.key # once we reach a node with no right child then this node is the maximum value

# lets build our tree and finf min adn max
"""
     10
    /  \
   5   20
       / \
     15  100 
"""  
  
root = BST(None) # creating empty tree
# insterting all our nodes
root.insert(10)
root.insert(5)
root.insert(20)
root.insert(15)
root.insert(100)
root.min_node() # 5
root.max_node() # 100


# ! Implementing Heap Tree in Python (see details on heap tree in tree types notes)
# EX of heap tree (note both are complete Binary trees):
# min heap (the parent node is less than or equal to its children and so the root node is the min value):
""" 
     1
    / \
   4  10
  / \
70  100 
    /  \
  120  120
"""
# max heap (the parent node is greater than or equal to its children and so the root node is the max value):
""" 
     100
    /   \
   50   70 
  / 
10   
"""

# ! Operations on Heap Tree

# ! Heapify
# * Heapify is a process of converting a non-heap tree into a heap tree or updating the heap tree to maintain the heap property it also allows us to create min or max heap from a complete Binary tree
# * we use the heapify funtion when we insert or delete a node and when we want to create a bianry heap from a array
# * heapify has two types: 
# 1) heapify up (from bottom to top, we compare node with its parent making sure the nodes are following heap propertie is not we will rearrange it) 
# 2) heapify down (from top to bottom, we compare node with its children making sure the nodes are following heap propertie is not we will rearrange it)
# when comparing we swap the nodes if they are not following the heap property
# EX of not heap to heap (heapify down) after comparing we go down the tree
"""
   10          2
  /  \   =>   / \
2     6     10   6
""" 
# * if we are dealing with a min heap its min heapify, if we are dealing with a max heap its max heapify

# ! Insertion (while mainting heap property)
# 1) we add the new node to the first open stop avalible in the lower level (last level) of the tree (we insert here to maintain the complete binary tree property)
# 2) check if this new node is following the heap property, if not we will use the heapify up function to rearrange it. (we use heapify up to maintain the heap property)
# Ex of inserting from [4, 1, 6] in MAX HEAP; we first insert 3 as root then we insert 2 at the first open spot (to the left of 4) so far its still max heap when we check using heapify as parent is greater than child 4>2
# after inserting 6 to the next avalible spot (left to right so its right of 4) we check using heapify if its still heap and its not so we swap 4 and 6 (4<6) so now its max heap
""" 
  4           6
 /  \   =>   / \
1     6     1   4
"""

# ! Deletion (while mainting heap property)
# * for all nodes 
# 1) we delete the node we want by replacing it with the last node in the tree (which is the right most node in the tree)
# 2) delete the last node which is now in the deleted nodes position
# 3) heapify the replaced node to maintain the heap property

# ! min or max node
# if we have map heap the max node is the root and the min node is the last node in the tree (on left or right)
# if we have min heap the min node is the root and the max node is the last node in the tree (on left or right)

# ! creating a min or max heap from a array 
# williams method:
# 1) we create an empty heap tree
# 2) insert each element of the array into the heap tree one by one
# 3) after each insertion we heapify the tree to maintain the heap property

# we will fo the second method
# 1) we create a complete binary tree using the given array of numbers
# 2) we will start from the last internal node we will heapify the tree at each node, comparing the node with its children and rearranging them if they are not following the heap property
# 3) a internal node is a node which has children so the las tinternal node is the last node in the tree that has children, we start here as leaf node has no children so nothing to compare with when heaping
# NOTE: we need to heapify the tree depending on the type of heap we are creating (min or max heap)

# ! creating a list of numbers from a binary tree (list representation of binary tree)
# NOTE: since a heap tree is a complete binary tree we know exactly how many nodes are in each level of the tree expect the last level which can vary
# at level 0 we have 1 node (the root) at level 1 we have 2 nodes (the children of the root) at level 2 we have 4 nodes so it will grow by a factor of 2 ie double each time but the last level can be full or have one node or anything in between
# Building the list: 
# 1) store the root node at the first position in the list index 0
# 2) store the children of the root node at the next two positions in the list index 1 and 2 with left child at index 1 and right child at index 2
# 3) now we look at the left child of the last node or gandchild or root and add its children to the list at the next two positions in the list with the left child at index 3 and right child at index 4 and then move onto the right grandchild of root and store its children in the next indexes before moving onto the left child of the leftgrandchild of root and so on
# 4) we do this for all levels and since we go left to right the numebr of nodes at the last level dose not matter
# 5) once we run out of nodes we stop and list is ready
# * NOTE: this is the level order traversal of the binary tree

# * now we can find the position in the heap tree of any node in the list using the formuals:
# 1) root = list[0]
# - let ith node be at position i in the list ith node = list[i] then:
# 2) the parent node of ith node = list[(i-1)//2] # '//' is integer division so 3//2 = 1
# 3) the left child of ith node = list[(2*i)+1] 
# 4) the right child of ith node = list[(2*i)+2]

# ! Heap queue 
# * a heap queue is a data structure that is a combination of a queue and a heap specifically a min heap
# * used to implement priority queues where elements are inserted with a priority (higher priority items are processed first)
""" 
# NOTE: Heap trees can have key, value pairs wher the key is used for the priority and the value is used for the data
# Here we only use the key for the priority and the value is not used but the node objects can have a value and key pair (see priority queue)
"""

# * we will first use the heapq python module to implement a heap queue as we will get methods like heapify and insert by importing heapq
import heapq # importing the heapq module

# * we will now use lists to implement a heap queue
heap = [] # creating an empty list for the heap queue

# using heapq to make this min heap tree:
""" 
     1
    / \
   4  10
  / \
70  100 
"""
# note the order of insertion dose not matter the heapify method will rearrange the elements to maintain the heap property
heapq.heappush(heap, 1) # adding 5 to the heap queue this methods ensures we insert 5 into the list 'heap while maintaining the min heap property
heapq.heappush(heap, 4) # adding 4 to the heap queue here 4 will be inserted after 1 as the min heap property is => the child is greater than parent
heapq.heappush(heap, 10) # adding 4 to the heap queue here
heapq.heappush(heap, 70) # adding 10 to the heap queue here
heapq.heappush(heap, 100) # adding 70 to the heap queue here

# to remove an element from the heap queue we use the heappop method, NOTE the pop alwasy removes the root node
heapq.heappop(heap) # removing the root node 1 from the heap queue
# new tree note that 4 will be new root as all children must be greater than parent and 100 is in the left of 70 as we fill the left subtree first (i.e fill the left most node first before moving right)
""" 
     4
    / \
   70  10
  /
100 
"""
# the heap queue = [4, 70, 10, 100] note now the first 3 elements are [root, lchild, rchild, lgrandchild or lchild of lchild]

# converting any list to a heap queue using the heapify method
list = [1, 4, 10, 70, 100] # creating a list of numbers
heapq.heapify(list) # converting the list to a heap queue 
# list = [1, 4, 10, 70, 100] # same as original heap tree example

# we also have heappushpop() method which is a combination of heappush() and heappop() and etc

# we can also pop then push to replace the root but there is a method for this called replace
# this method will pop the smallest element (root) and add the new element at the correct position
heapq.heapreplace(heap, 20) # removes root and adds 20 to the corretn position (after 10)
# heap = [10, 70, 20, 100]
# tree is now
""" 
     10
    /  \
   70   20
  /
100 
"""

# we can also get teh nth smallest element meaning if n = 2 we will get the 2 smallest elements in the heap queue with index[list.len-1] being the 2nd smallest element and index[0] being the 1st smallest element
heapq.nsmallest(2, heap) # getting the 2 smallest elements in the heap queue = [10, 20]
# * note this methos works on any iterable object not just heap trees

# we can do the same thing to get nth largest numbers
heapq.nlargest(2, heap) # getting the 2 largest elements in the heap queue = [100, 70]

# ! priority queue, using heapq
# NOTE: a priority queue is a queue where the elements are ordered based on their priority each element has a data and value to beused in determining the priority "see the priority Queue.py for more"
# NOTE: smallest element is always at the front of the queue meaning => SMALLEST VALUE = HIGHEST PRIORITY so the smallest value is always popped first ie removed first from the queue
# * since a heap queue is a min heap this means the smallest element is always at the root of the tree and hence the first element in the priority queue this means we can remove the smallest element from the queue using the heappop method and then hepify the queue to maintain the heap property and repeat this process
priority_queue = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] # creating a list of tuples where each tuple has a data and value to be used in determining the priority the order dose not matter
heapq.heapify(priority_queue) # converting the list to a heap queue note that now each tuple is ordered based on the value of the tuple with the smallest value at the root of the tree

# pop i.e remove the elements from the queue to the the order of the queue mening the order the elements should be removed here the highest proirity is 1 and is given to 'a
for i in range(len(priority_queue)):
  print(heapq.heappop(priority_queue)) # removing the elements from the queue in the order of priority as we heapify the priority queue beforehand this will print the elements in the order of priority
  
""" 
output:
(1, 'a') = > highest priority
(2, 'b')
(3, 'c')
(4, 'd') = > lowest priority
"""

# ! Quad-Trees
"""
Quad-Trees:
A Quad-tree is a tree data structure used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.
It is used for spatial indexing and range queries.

Explanation:
1. The Quad-tree starts with a single root node representing the entire area.
2. The node is subdivided into four child nodes, each representing a quadrant.
3. Each node in the tree contains either a point or a small number of points. If a node has more than the maximum allowed points, it is subdivided further.
4. Quad-trees are useful for handling 2D spatial data like images, maps, and game environments.

Key operations:
- Insertion: Points are added to the tree, and if a quadrant exceeds capacity, the node is subdivided.
- Searching: Queries like range searches can be efficiently performed using the tree structure.
- Deletion: Points can be deleted from the tree, and rebalancing is performed if necessary.

Example:
Consider a 2D grid divided into 4 quadrants:
Quadrant 1: (0, 0) to (5, 5)
Quadrant 2: (5, 0) to (10, 5)
Quadrant 3: (0, 5) to (5, 10)
Quadrant 4: (5, 5) to (10, 10)

A Quad-tree can index points in this space and perform range queries for points within specific quadrants.
"""

# Code: Quad-tree example (simplified)
class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary  # The rectangular boundary (x_min, y_min, x_max, y_max)
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        if not self._in_boundary(point):
            return False
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        if not self.divided:
            self.subdivide()
        return (self.nw.insert(point) or self.ne.insert(point) or self.sw.insert(point) or self.se.insert(point))

    def _in_boundary(self, point):
        x, y = point
        x_min, y_min, x_max, y_max = self.boundary
        return x_min <= x < x_max and y_min <= y < y_max

    def subdivide(self):
        x_min, y_min, x_max, y_max = self.boundary
        mx = (x_min + x_max) / 2
        my = (y_min + y_max) / 2
        nw_boundary = (x_min, y_min, mx, my)
        ne_boundary = (mx, y_min, x_max, my)
        sw_boundary = (x_min, my, mx, y_max)
        se_boundary = (mx, my, x_max, y_max)
        self.nw = QuadTree(nw_boundary, self.capacity)
        self.ne = QuadTree(ne_boundary, self.capacity)
        self.sw = QuadTree(sw_boundary, self.capacity)
        self.se = QuadTree(se_boundary, self.capacity)
        self.divided = True

# Test the Quad-tree
qt = QuadTree((0, 0, 10, 10))
qt.insert((1, 1))
qt.insert((7, 8))
qt.insert((3, 4))

"""
Analysis:
1) We insert (1, 1). It is within the boundary, so it is added to the root.
2) We insert (7, 8). It is within the boundary, so it is added to the root.
3) We insert (3, 4). It is within the boundary, so it is added to the root.
4) If we insert more points and exceed the capacity, the root will subdivide into four quadrants.
"""

# ! R-Trees
"""
R-Trees:
An R-Tree is a tree data structure used for indexing multi-dimensional information such as geographical coordinates, rectangles, or polygons.
It is often used for spatial data and is an efficient method for searching within multidimensional space.

Explanation:
1. The R-tree is a balanced tree in which each node contains a bounding box that contains all of its child nodes.
2. The leaf nodes contain the actual data objects (e.g., rectangles, polygons).
3. The non-leaf nodes store bounding boxes that cover all the child nodes and are used to guide the search.
4. R-trees allow for efficient spatial queries such as range searches and nearest neighbor searches.

Key operations:
- Insertion: New elements are inserted into the tree, and if necessary, a split occurs to maintain balance.
- Searching: The tree can quickly search for objects within a given range.
- Deletion: A deleted object is removed, and the tree may require rebalancing.

Example:
Consider the following bounding boxes in 2D space:
Box1 = (0, 0, 5, 5)
Box2 = (1, 1, 4, 4)
Box3 = (3, 3, 6, 6)

The R-tree can index these boxes and perform spatial queries.
"""

# Code: R-tree example (simplified)
class RTree:
    def __init__(self, max_nodes=4):
        self.max_nodes = max_nodes
        self.root = []

    def insert(self, box):
        # Inserting a bounding box into the R-tree
        if len(self.root) < self.max_nodes:
            self.root.append(box)
        else:
            # Simple logic for inserting and splitting
            self.root = [self.root, [box]]  # Splitting

    def search(self, query_box):
        # Searching for a bounding box that intersects with the query_box
        results = []
        for box in self.root:
            if self._intersects(query_box, box):
                results.append(box)
        return results

    def _intersects(self, box1, box2):
        # Check if two boxes intersect
        return not (box1[2] < box2[0] or box1[0] > box2[2] or box1[3] < box2[1] or box1[1] > box2[3])

# Test the R-tree
rtree = RTree()
rtree.insert((0, 0, 5, 5))
rtree.insert((1, 1, 4, 4))
rtree.insert((3, 3, 6, 6))

# Searching for bounding boxes intersecting with (2, 2, 4, 4)
print(rtree.search((2, 2, 4, 4)))

"""
Analysis:
1) We insert (0, 0, 5, 5). It is added to the root.
2) We insert (1, 1, 4, 4). It is added to the root.
3) We insert (3, 3, 6, 6). It is added to the root.
4) When searching for (2, 2, 4, 4), it intersects with (0, 0, 5, 5) and (1, 1, 4, 4).
"""

# ! B-Trees
"""
B-Trees:
A B-tree is a self-balancing tree data structure that maintains sorted data and allows efficient insertion, deletion, and searching in logarithmic time.
It is commonly used in databases and file systems.

Explanation:
1. A B-tree is a multi-level index structure. Each node can contain multiple keys and child pointers.
2. Internal nodes guide the search process, while leaf nodes contain the actual data or references to data.
3. B-trees are balanced, meaning that the height of the tree is minimized for fast search performance.
4. The number of keys in each node must follow certain rules (e.g., a minimum and maximum number of keys per node).

Key operations:
- Insertion: Keys are inserted into the tree while maintaining balance.
- Searching: The tree allows efficient searching in logarithmic time.
- Deletion: Keys can be removed while ensuring that the tree remains balanced.

Example:
Consider a B-tree with a minimum degree of 2, where each node can hold 3 keys and has 4 child pointers. Inserting keys will split nodes when necessary to keep the tree balanced.
"""

# Code: B-tree example (simplified)
class BTree:
    class Node:
        def __init__(self, leaf=False):
            self.keys = []
            self.children = []
            self.leaf = leaf

    def __init__(self, t=2):
        self.t = t  # Minimum degree (defines the range for the number of keys)
        self.root = self.Node(leaf=True)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            s = self.Node()
            s.children.append(self.root)
            self._split(s, 0)
            self.root = s
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self._split(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split(self, parent, i):
        node = parent.children[i]
        new_node = self.Node(leaf=node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys[self.t - 1])
        new_node.keys = node.keys[self.t:]
        node.keys = node.keys[:self.t - 1]
        if not node.leaf:
            new_node.children = node.children[self.t:]
            node.children = node.children[:self.t]

# Test the B-tree
btree = BTree(t=2)
btree.insert(10)
btree.insert(20)
btree.insert(5)

"""
Analysis:
1) We insert 10. It is added to the root.
2) We insert 20. It is added to the root.
3) We insert 5. It is added to the root.
4) If we insert more keys and exceed the capacity, the root will split, and the tree will rebalance.
"""
