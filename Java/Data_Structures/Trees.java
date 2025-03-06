/* 
# ! a tree is a non linear data structure meaning unlike a list the next element dosent alwasy have to be left or right after another it can be anywhere but all the nodes must be connected
# ! there can also he a hierircy to trees meaning a node can have a parent and children nodes and a child node can have children nodes and so on.
# ! a tree is a recursive data structure meaning they can be divided into sub trees
# ! in a tree there can only be 1 path between 2 nodes, if there are more than 1 path then its a graph not a tree. this means 2 nodes cannot point to each other in a tree. only from one node to another.

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

- **Ancestor**: A node that lies on the path between the root and a given node. For example, `[Root]` is an ancestor of `[Great Grandchild 1]`. NOTE: the root is the ancestor of all nodes in the tree. for '[great grandchild 1]' the number of ancestors is 4 (root, child 1, grandchild 1, great grandchild 1) this is the ancestor path for '[great grandchild 1]'. this path for every node will be unique.

- **Descendant**: A node that lies on the path between the root and a given node. For example, `[Great Grandchild 1]` is a descendant of `[Root]`. NOTE: all nodes in the tree are descendants of the root. for 'Child 1' the number of descendants is 5 (child 1, grandchild 1, great grandchild 1, grandchild 2, child 3) since there are many descendants we can take multiple paths as we have multiple descendants so the decentant path for 'Child 1' is not unique.

- **Neighbors**: In a graph, a neighbor node is any node that is directly connected by an edge. here child 1 is a  neighbor of root, GC1 and GC2

- **Subtree**: A tree consisting of a node and all its descendants. For example, the subtree rooted at `[Child 1]` includes `[Child 1]` (the subtrees new root), `[Grandchild 1]`, `[Grandchild 2]`, and `[Great Grandchild 1]`. NOTE: for the subtree at child 1 the grandchild 1 would acctualy be a child of child 1 if we were to traverse it. NOTE: every next node will have its own subtree or subtrees on left right etc. The smallest subtree is a leaf node and the largest subtree at the root. The Number of subtrees in a tree is equal to the number of nodes in the tree.

- **Height**: The height of a node in a tree is the number of edges in the longest path from the node to a leaf (known as the path). For example, the height of `[Root]` is 3 (from root to GGC1). the height of '[Child 1]' is 2 (from child 1 to GC1). Dont confuse with depth. Depth is from the root to the node height is from the node to the leaf node. NOTE: the height of a tree is the height of the root node.

- **Depth/Level**: The depth of a node is the number of edges from the root to that node (known as the path). The root node has a depth of 0, its children have a depth of 1, and so on. NOTE: the depth starts at 0 and the depth of the tree (max depth) is the length of the longest path from the root to a leaf, so the max depth of this tree is 3 (from root to GGC1) = to the number of edges in that path = depth of the tree, Dont confuse with height. Depth is from the root to the node height is from the node to the leaf NOTE: the depth of a tree is the depth of the leaf node.

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
     - In a full binary tree, every node other than the leaves has exactly two children meaning any node can have 2 children or 0 children (making it a leaf).
     - In a complete binary tree, all levels of the tree except the last level are completely filled (meaning must have 2 child nodes). Last level can be either completely filled or filled left to right meaning that if the last level has 2 child nodes they must be on the left most node of the previous level. if we have one node it must be a left node to the left most node of the previous level. This left most node must be filled first before moving to the right
     - In a Perfect binary tree, all the nodes except for leaf nodes have 2 children and all the leaf nodes are at the same level.
     - In a Balanced binary tree, the difference in height between the left and right subtrees of every node is at most 1. This means at each node the left and right subtrees must be as close to the same height as possible.
     - In a pathalogical binary tree, every parent node has only 1 child node.
     - total number of nodes = num of nodes in left subtree + num of nodes in right subtree + 1. (+1 for the root node)
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
           and we will do steps 2 and 3 on both left and right nodes over and over Recursilvely until we run out of nodes meaning the node is a leaf node. NOTE: the step 1 is checking the root but here the root is the left or right subtree of the prevoius root. 
           so after printing this root which is on the left or right subtree we will do the same steps on the left node of this left node until  we run out of nodes on the left subtree then we go right and check for left children on this right node until we run out of left children on this right node then we go right on this right node and do the same steps until we have no left children on this right node we repete this until we run out of nodes
           EX: in the first ex tree after first run we will get in this order: (Root, Child1, G1, GG1, G2, C2, C3) at each root we alwasy fully traverse all the left nodes of each left nodes (ie the left subtree) when we run out of left nodes we go right this is our new root and we must first now cehc kif this root has a left serch the left like befrore if it dose then once we run out we go right. and so on until we are done with all the nodes.
      - 2. In order Traversal: (Given a Non Empty BST) Traverse the left subtree (at first left most node, it will be on left side of root), then the root node (at first is the root of our left most node we just traversed), then the right subtree (at first the node right of the root). DO THIS RECURSIVLY! meaning after going to thr right node we must go to the left most node of this right node and so on until we run out of nodes meaning the node is a leaf node
           EX: in the first ex tree after first run we will get in this order: (GG1, G1, C1, GC2, Root, c2, c3) note how from the left most node we bo back up checking to see if we can go right after finishing the right subtree we go right back where we branched right and move back once more
           once we reach the root of bst we do the. NOTE!: by doing this traversal we will get the values in order smallest to largest
      - 3. Post order Traversal: (Given a Non Empty BST) Traverse the left subtree (at first the left most node on left side of root), then the right subtree (going to the right most node of this prevoius left node), then the root node (the curretn node it will have no left or right child). DO THIS RECURSIVELY at each node! just like before after this step the new root node will
           EX from tree: (GG1, G1, G2, C1, C3, C2, Root) note how we go to left most then backwards until we reach a node with right node and do the same first step of going as left as we can and repeting.
      - 4. Breadth First Traversal: (Given a Non Empty BST) Traverse each level of the tree from left to right then move onto the next level do this from top to bottom (level 0 to level n). DO THIS RECURSIVELY! EX from tree: 1) root, 2) Child one and child two 3) GC 1 and GC2 and Child 3 and so on. going level by level in each level left to right. NOTE: this is the only traversal that is linear. 
      - 5. Depth First Traversal: (Given a Non Empty BST) Traverse the tree in a depth first manner. meaning starting a the root visit any neigbour node and keep doing deaper traversing each neighbours neighbours until you reach a node with no unvisited neighbors (leaf), backtrack to the last node with unvisited neighbors. Repeat until all nodes are visited. EX: root, Child, G1, GG1, G2, Child 2, Child3

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
   NOTE: complete BT => all levels of the tree except the last level are completely filled or filled left to right meaning the left most node of each level is filled first, heap property => for any given node, the parent node is either greater than (max heap) or less than (min heap) the children node, so if every node is greater than or equal to its children its max heap or if its less than or equal to its children its min heap.
   this implies that for max heap the root node is the max value and for min heap the root node is the min value. ! this rule for heap must be true for all nodes in the tree.
   - Characteristics:
     - **Max-Heap**: The value of each node is greater than or equal to the values of its children.
     - **Min-Heap**: The value of each node is less than or equal to the values of its children.
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
*/

package Java.Data_Structures;
import java.util.ArrayList;

/* 
Implementation of Trees in Java: (BST vs General Tree)
-------------------------------
- Each tree type will have its own implementation based on the specific properties and rules of that tree.
- Along with that the node will have its own implementation with its own properties and methods.
EX: for BST the node has data and left and right nodes. while a general tree node can have data and a list of children nodes.
EX: a BST's serch node function will check wether the node is found or not and if not will branch to the left or right subtree depeneding on the value of the node.
  in a general tree the search node function will check if the node is found or not and if not will branch to the children nodes and repeat the process until the node is found or we run out of nodes.
*/

// General Tree using arraylist
class TreeNode<T> {
  private T data;
  private TreeNode<T> parent; // Changed from T to TreeNode<T>
  ArrayList<TreeNode<T>> children;

  public TreeNode(T data) {
    this.data = data;
    this.parent = null;
    this.children = new ArrayList<>();
  }

  public T getData() {
    return this.data;
  }

  public TreeNode<T> getParent() { // Changed return type from T to TreeNode<T>
    return this.parent;
  }

  public void setData(T data) {
    this.data = data;
  }
  public void addChild(TreeNode<T> child) {
    this.children.add(child);
  }
  public void removechild(TreeNode<T> child) {
    this.children.remove(child);
  }
  
  public void setParent(TreeNode<T> parent) { // Changed parameter type from T to TreeNode<T>
    this.parent = parent;
  }

  public int depth(TreeNode<T> node) {
    if (node.getParent() == null) {
      return 0;
    }
    else{
      return 1 + depth(node.getParent());
    }
  }
}




public class Trees {
  public static void main(String[] args) {
  // constructing a general tree
  TreeNode<Integer> root = new TreeNode<>(1);
  TreeNode<Integer> node2 = new TreeNode<>(2);
  TreeNode<Integer> node3 = new TreeNode<>(3);

  // connecting the nodes
  root.addChild(node2); // This will automatically set the parent if you use the modified addChild
  root.addChild(node3); // This will automatically set the parent if you use the modified addChild
  node2.setParent(root); // This will automatically set the parent if you use the modified addChild
  node3.setParent(root); // This will automatically set the parent if you use the modified addChild
  }
    
}
