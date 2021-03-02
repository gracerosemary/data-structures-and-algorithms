# Data Structures and Algorithms

## Language: `Python`

# Binary Tree - FizzBuzz edition
[Click to be directed to Code Challenge](https://github.com/gracerosemary/data-structures-and-algorithms/tree/master/python/challenges/fizz_buzz_tree)      

## Challenge
1. Write a function called `fizzbuzztree` which takes binary tree as argument.  
2. Determine whether or not the vlaue of each node is divisible by 3, 5, or both.  
3. Create a new tree with the same structure as the original tree but with modified values:  
      - if value is % 3, replace value with “Fizz”  
      - if value is % 5, replace value with “Buzz”  
      - if divisible by both, replace with “FizzBuzz”  
      - if not divisible, turn the number into a String  
 4. Return the new tree  

## Tests
Output a list for FizzBuzz. 
Output a list for Fizz. 
Output a list for Buzz. 
Output a list for String. 
Exception for empty tree. 

## Approach & Efficiency
time: O(n) - needs to traverse through 'n' nodes
space: O(1) - traversing through tree does not need any additional space allocation

## API
Node class:
- `init`: instantiate with constructors

BinaryTree class:
- `init`: instantiate with constructors
- `change_vals`: changes the value of the node based on if it's divisible by 3, 5, or both.  
- `fizzbuzztree`: traverses the tree and appends new values to a list before returning the list.  

## Solution
![Solution Image](assets/fizzbuzz.png)   