# Data Structures and Algorithms

## Language: `Python`

# Binary Tree and BST Implementation
[Click to be directed to Code Challenge](https://github.com/gracerosemary/data-structures-and-algorithms/tree/master/python/challenges/tree)      

## Challenge
Node class: has properties for the value stored in the node, the left child node, and the right child node.  

BinaryTree class: preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
 
BinarySearchTree class: add and contains method that adds a value and returns Boolean if tree contains a specified value. 

## Tests
Can successfully instantiate an empty tree  
Can successfully instantiate a tree with a single root node  
Can successfully add a left child and right child to a single root node  
Can successfully return a collection from a preorder traversal  
Can successfully return a collection from an inorder traversal  
Can successfully return a collection from a postorder traversal  

## Approach & Efficiency
BinaryTree methods use recursion, which has a Big O time complexity of O(n), because we have to traverse the entire tree (look at 'n' items). The space complexity for height is log n while width is O(w). 

BinarySearchTree has a Big O time complexity of O(h) since in the worst case scenario, we will have to search the entire height of the tree. Space would be O(1) because we do not allocate any additional space for a search. 

## API
Node class:
- `init`: instantiate with constructors

BinaryTree class:
- `init`: instantiate with constructors
- `preOrder`: Root >> Left >> Right
- `inOrder`: Left >> Root >> Right
- `postOrder`: Left >> Right >> Root

BinarySearchTree class:
- `contains`: Returns True if value is in the tree, otherwise False
- `add`: Accepts a value and adds a new node with the specified value in the correct location