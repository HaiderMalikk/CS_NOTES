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
   - Uses: Efficient searching, insertion, and deletion of elements with an average time complexity of O(log n) when balanced; used in applications requiring sorted data, such as databases.

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

