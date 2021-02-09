# Data Structures and Algorithms

## Language: `Python`

# Binary Tree - Find Max Value
[Click to be directed to Code Challenge](https://github.com/gracerosemary/data-structures-and-algorithms/tree/master/python/challenges/tree)      

## Challenge
Write a breadth first traversal method which takes a Binary Tree as its unique input. Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Tests
Output a list for a tree with 1 node. 
Output a list for a tree with even number of nodes. 
Output a list for a tree with odd number of nodes. 

## Approach & Efficiency
time: O(n) - needs to traverse through 'n' nodes
space: O(1) - traversing through tree does not need any additional space allocation

## API
Node class:
- `init`: instantiate with constructors

BinaryTree class:
- `init`: instantiate with constructors
- `preOrder`: Root >> Left >> Right
- `inOrder`: Left >> Root >> Right
- `postOrder`: Left >> Right >> Root
- `findMaximumValue`: returns max value in Binary Tree
- `breadth_first`: takes in a binary tree and returns a list

BinarySearchTree class:
- `contains`: Returns True if value is in the tree, otherwise False
- `add`: Accepts a value and adds a new node with the specified value in the correct location

## Solution
![Solution Image](assets/breadth.png)  