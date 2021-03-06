# Data Structures and Algorithms

## Language: `Python`

# Graph - Breadth First Search
[Click to be directed to Code Challenge](https://github.com/gracerosemary/data-structures-and-algorithms/tree/master/python/challenges/breadth_first)       

## Challenge
`AddNode()`: Adds a new node to the graph. Takes in the value of that node. Returns the added node.  
`AddEdge()`: Adds a new edge between two nodes in the graph. Include the ability to have a “weight”. Takes in the two nodes to be connected by the edge. Both nodes should already be in the Graph.  
`GetNodes()`: Returns all of the nodes in the graph as a collection (set, list, or similar)  
`GetNeighbors()`: Returns a collection of edges connected to the given node. Takes in a given node. Include the weight of the connection in the returned collection.  
`Size()`: Returns the total number of nodes in the graph.  
`breadth_first()`: Accepts a starting node and returns a collection of nodes in the order they were visited.  
 
## Tests
- One node
- Multiple nodes
- Island node

## Approach & Efficiency
time = O(n)   
space = O(1)       

## Solution
![Solution Image](assets/bfs_graph.png)  