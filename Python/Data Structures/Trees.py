# ! Trees in python
# ! a tree is a non linear data structure meaning unlike a list the next element dosent alwasy have to be  or right after another it can be anywhere, there can also he a hierircy to trees
# ! a tree is a recursive data structure meaning they can be divided into sub trees
# ! ex of a tree and its properties 
"""
A simple representation of a tree data structure.

Example Tree Structure:

             [Root]
            /      \
        [Child 1]   [Child 2]
        /       \            \
[Grandchild 1] [Grandchild 2] [Child 3]
    |
[Great Grandchild 1]

Tree Properties:
----------------
- **Node**: Each individual element of the tree. A node can contain a value and links to other nodes (its children).

- **Edge**: An edge connects a parent node to a child node. In a tree, each edge represents a link that allows traversal between nodes basicaly a edge connects 2 nodes and is a path between them. NOTW: Number of edges = number of nodes - 1

- **Path**: A sequence of nodes in a tree that connects a two nodes. here the path between root and grandchild 2 is: [Root] → [Child 1] → [Grandchild 2]. NOTE: there are only one unique path between 2 nodes in a tree. 

- **Root**: The topmost node of the tree. There is only one root node in a tree. It serves as the entry point for traversal.

- **Leaf**: A node that does not have any children. In the above structure, `[Great Grandchild 2]` and `[Child 3]` are leaf nodes. NOTE: a non leaf node would be a parent node.

- **Children**: The nodes that are directly connected to a given node when moving away from the root. For example, `[Child 1]` and `[Child 2]` are children of `[Root]`. NOTE: a child node can have only 1 parent

- **Parent**: The node that has one or more children. For instance, `[Root]` is the parent of `[Child 1]` and `[Child 2]`. NOTE: a parent node can have multiple children

- **Sibling**: Nodes that share the same parent. `[Child 1]` and `[Child 2]` are siblings since they share the same parent `[Root]` notice how there on the same level.

- **Subtree**: A tree consisting of a node and all its descendants. For example, the subtree rooted at `[Child 1]` includes `[Child 1]` (the subtrees new root), `[Grandchild 1]`, `[Grandchild 2]`, and `[Great Grandchild 1]`. NOTE: for the subtree at child 1 the grandchild 1 would acctualy be a child of child 1 if we were to traverse it. NOTE: every next node will have its own subtree or subtrees on left right etc.

- **Height**: The height of a tree is the length of the longest path from the root to a leaf. The height of a tree is measured in edges (or nodes, depending on definition). NOTE: the height starts at 0 so here the height is 3, at height 0 we have root at height 3 we have great grandchild 1.

- **Depth**: The depth of a node is the length of the path from the root to that node. The root node has a depth of 0, its children have a depth of 1, and so on. NOTE: the depth starts at 0 and the depth of the tree (max depth) is the length of the longest path from the root to a leaf, so the max depth of this tree is 3 (from root to GGC1) = to the number of edges in that path = height of the tree

- **Degree of a node**: The degree of a node is the number of children it has. For example, the degree of `[Child 1]` is 2 (it has two children: `[Grandchild 1]` and `[Grandchild 2]`), while the degree of `[Child 2]` is 1 (it has one child: `[Child 3]`). 

- **Degree of a tree**: The degree of a tree is the maximum degree of any node in the tree or can be the max number of children that a particular node has. here root and child 1 have a degree of 2 while all others have 1 or 0 this means the degree of the tree is 2.
"""

# ! Trees can have many types, but only one type of data structure, by type of trees we mean binary trees or n-ary trees etc what makes these trees different is that they have different properties meaning they have different shapes and structure and rules.
# ! here are some common tree structures and descriptions
"""
Tree Types Overview:
0. **General Tree**:
   - Definition: A tree in which each node can have any number of child nodes i.e there is no limit on the number of child nodes a node can have.
   - Characteristics:
     - any node can have any number of children.
     - the tree above given in teh example is a general tree.
   - Uses: Various.

1. **Binary Tree**:
   - Definition: A tree in which each node has at most two children, referred to as the left child and the right child.
   - Characteristics: 
     - Each node can have 0, 1, or 2 children.
     - The height of a balanced binary tree is minimal for a given number of nodes.
     - In a full binary tree, every node other than the leaves has exactly two children meaning any node can have 2 children or 0 children (making it a leaf).
     - In a complete binary tree, all levels of the tree except the last level are completely filled (meaning mus thave 2 child nodes). Last level can be either completely filled or filled left to right meaning that if the last level has 2 child nodes they must be on the left most node of the previous level. if we have one node it must be a left node to the left most node of the previous level. This left most node must be filled first before moving to the right
     - In a Perfect binary tree, all the nodes except for leaf nodes have 2 children and all the leaf nodes are at the same level.
     - In a Balanced binary tree, the difference in height between the left and right subtrees of every node is at most 1.
     - In a pathalogical binary tree, every parent node has only 1 child node.
     - total number of nodes = #of nodes in left subtree + #of nodes in right subtree + 1. (+1 for the root node)
   - Uses: Commonly used in various applications such as expression trees for evaluating mathematical expressions and heaps for efficient data storage.

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
      - 1. Pre order Traversal: (Given a Non Empty BST) Visit the root node, then the left subtree(left child of root), then the right subtree(right child of root). DO THIS RECURSIVELY! meaning the node on left and right subtree will become the new root node 
           and we will do steps 2 and 3 on both left and right nodes over and over Recursilvely until we run out of nodes meaning the node is a leaf node. NOTE: we dont do step one as we alredy checked the left and right nodes of the root node so when the 
           child nodes become the root node they would have alredy been treversed. EX: in the first ex tree after first run we will get in this order: (Root, Child1, Child2) now new root is child 1 once we run out of nodes on left side (child1) we move on to our second root node Child 2 (right subtree)
      - 2. In order Traversal: (Given a Non Empty BST) Traverse the left subtree (at first left most node on left side of root), then the root node (at first is the root of our left most node we just traversed), then the right subtree (at first the node right of the root). DO THIS RECURSIVLY!  
           EX: in the first ex tree after first run we will get in this order: (GG1, G1, null) since G1 has no right node we are done step one NEW root is child one (the new left node would be the parent of the prevoius root but since we alredy travered this new left node as root in the last iteration we dont count it ). 
           once we reach the root of bst we do the. NOTE!: by doing this traversal we will get the values in order smallest to largest
      - 3. Post order Traversal: (Given a Non Empty BST) Traverse the left subtree (at first the left most node on left side of root), then the right subtree (at first right of the root), then the root node (at first parent of left and right nod we just traversed). DO THIS RECURSIVELY at each node! just like before after this step the new root node will
           be the parent of the rprevoius root node but now our new left node was arlerdy traversed as the root node last time so we dont count it EX from tree: (GG1, null, G1) since G1 has no right node we are done step new root node is child one (the new left node is G1 but since we traverd it last time as our root we skip it).
      - 4. Level order Traversal: (Given a Non Empty BST) Traverse each level of the tree from left to right then move onto the next level do this from top to bottom (level 0 to level n). DO THIS RECURSIVELY! EX from tree: 1) root, 2) Child one and child two 3) GC 1 and GC2 and Child 3 and so on. going level by level in each level left to right. NOTE: this is the only traversal that is linear. 

    - Min and Max values (nodes): (Given a Non Empty BST) The min value is the smallest value in the BST and will be in the left subtree. The max value is the largest value in the BST  and will be in the right subtree. IF no left node or IF no right node then root is the smaller or larger value respectively.
      since each time a new node is made the smaller child is on the left this means the smallest value will be on the left most node of the tree. same logic for max value it will be on the right most node. EX: in the first ex tree assuming its a BST like we said: Min = GG1, Max = Child 3
      to find it manually we would treverse the trees left and right subtrees and find the smallest and largest value by traversing untill no left or right node exits the nwe will know that our currrent node is a minimum or maximum node respectfully.

3. **Balanced Trees**:
   - Definition: Trees that automatically keep their height minimal, such as AVL trees and Red-Black trees.
   - Characteristics:
     - Height balancing ensures efficient operations like search, insert, and delete (O(log n)).
     - AVL trees maintain a strict balance factor, while Red-Black trees use color properties to ensure balance.
   - Uses: Often used in database indexing, memory management systems, and applications requiring frequent insertions and deletions.

4. **N-ary Tree**:
   - Definition: A tree in which each node can have at most N children.
   - Characteristics:
     - More flexible than binary trees, allowing multiple children, which can vary from node to node.
     - Useful for representing hierarchical data where a node can have an arbitrary number of children.
   - Uses: Suitable for representing hierarchical structures, such as file systems, organizational charts, and XML/JSON data representation.

5. **Trie (Prefix Tree)**:
   - Definition: A tree used for storing a dynamic set of strings where the keys are usually strings.
   - Characteristics:
     - Nodes represent prefixes of keys, allowing fast retrieval of strings based on common prefixes.
     - Each edge represents a character, and each path from the root to a leaf node represents a complete string.
   - Uses: Useful in applications like autocomplete features, spell checkers, and IP routing, where fast retrieval based on prefixes is necessary.

6. **Segment Tree**:
   - Definition: A tree used for storing intervals or segments, allowing efficient querying of overlapping segments.
   - Characteristics:
     - Each node represents a segment, and leaf nodes represent individual elements.
     - Allows querying which segments overlap with a given point efficiently, typically in O(log n) time.
   - Uses: Commonly used in computational geometry for finding range queries, updates, and interval problems, such as calculating the sum of elements over a given range.

7. **B-Tree**:
   - Definition: A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
   - Characteristics:
     - Nodes can have multiple children (more than two), and all leaves are at the same level.
     - It is designed to work well on disk and can handle large amounts of data efficiently, minimizing disk reads.
   - Uses: Used in databases and file systems for efficient data retrieval, ensuring that operations remain efficient even with large datasets.

8. **Heap Tree**:
   - Definition: A complete binary tree that satisfies the heap property, where each node has a specific order relative to its children.
   - Characteristics:
     - **Max-Heap**: The value of each node is greater than or equal to the values of its children.
     - **Min-Heap**: The value of each node is less than or equal to the values of its children.
     - Implemented as an array, where parent-child relationships are defined by indices.
   - Uses:
     - Efficiently implements priority queues, enabling quick access to the highest or lowest priority elements.
     - Forms the basis for the heapsort algorithm, sorting elements in O(n log n) time.
     - Utilized in graph algorithms, such as Dijkstra's algorithm, for efficient minimum element retrieval.
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

# in the repersentation below we can see what the tree above would look like in actual memory. each square is a node with key(data) left child and right child (the references to them) 
# once we get to the left child or right child we then have accsess to data and there children and the proccess is repeated until we reach a leaf node (recursively done).
# you can think of the edges (the path to the next node) as a pointer. with the reference we can go to the next node this reference is the path (simmilar to linked list).

# A repesentation of a BST in memory:
# NOTE: the ref is a random number repeseting the address of the object in memory for the sake of simplicity this address would give us the object so then we could access the data and the children
                         ____________
                        |  ref: 5100 |
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
    # create constructor, constructor makes teh object(in our case the node) our node has 3 properties: key, left child and right child 
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
      
    def insert(self, data): # create insertion method with data as input
        if self.key is None: # if root is empty ie key is nune note, key is the value of node. if there is no value meaning no key then there is no root node. EX: say we make BST(None) and call BST.insert(10) since at the moment of calling insert, the key of our BST is None, hence we have no root node. so we assign the BST obejcts key (its value) by using 'self.key' with data of 10. now the BST object has a key of 10 this the root node. 
            self.key = data  # if there is no root node then we assign the nodes key with the value of data. NOTE: we dont create a new node we just check if its null if it is then we assign the key to data. NOTE: this must the root as we cannot have empty nodes in the middle of the tree initially the key can be null and that will become teh root node once we assign it a value. 
            return # we stop the insertion process here as we have created the root node and are done with the insertion

        # if tree not empty check if the node is greater or less than the current node so we know wether to go to the left or right subtree
        # note that key is the value of our root note as we traverse the tree this root changes and we check if its greater or less than the current node recursively.
        if self.key > data: # goto left subtree as value of new node is less than current node 
          # here we must check if the left subtree is empty then we can dd the new node here. if its not emoty after travering some times we will reach the left subtree again and again untill we find a leaf nod at this leaf node the left child will be none and we can add the new node here
          if self.leftchild: # leftchild can be true or false but the condition only runs if its true that means we do have a left child
            # since we have a left child we must take the current node 'leftchild' as our new root node and do a insert again with the same value by calling the insert method on this leftnode (making it our root). 
            # when this function runs again and again at some point we will reach a leaf node then since we do still have a key(value) so if the comparison key > data is true (meaing we are still adding to left subtree) we will check if leftsubtree again but since the las troot node is a leaf node and its left child is none so now we can add the new node in the else block
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
            
    # ! dealing with duplicates
    # 1) we can add the follwing beofre branching: if key == data: return with this we do not add the node to the tree if the key is the same as the data we are trying to
    # 2) we can add the following at bracanging: if key > > data and key == data. or  if key < data and key == data. this way we add the node to the right or left subtree if the key is the same as the data we are trying to
          
    # ! Summary: 
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

# uncooment to see output
# print(root.key) # prints 10
# print(root.leftchild.key) # prints 5
# print(root.rightchild.key) # prints 20
# print(root.rightchild.leftchild.key) # prints 15
# print(root.rightchild.rightchild.key) # prints 100
# all the nodes are printed all nodes after will have value of NONE


  