# Data Structures and Algorithms

## Language: `Python`

# Hash tables
[Click to be directed to Code Challenge](https://github.com/gracerosemary/data-structures-and-algorithms/tree/master/python/challenges/hashtable)       

## Challenge
Implement a hash table with methods to hash a key/val pair, add a key/val pair, get/return a value given a key, and return a boolean if a key exists in the hash table.  

## Tests
Adding a key/value to your hashtable results in the value being in the data structure  
Retrieving based on a key returns the value stored  
Successfully returns null for a key that does not exist in the hashtable  
Successfully handle a collision within the hashtable  
Successfully retrieve a value from a bucket within the hashtable that has a collision  
Successfully hash a key to an in-range value  

## Approach & Efficiency
Big O Time: O(n) - key/val structure allows us to only search n number of elements (given a collision)  
Big O Space: O(n) - dependent on the number of elements stored  

## API
hash: Takes in an arbitrary key and returns an index in the collection.  
add: Takes both key and value. Hashes the key and adds the key and value pair to the table, handling conditions as needed. 
get: Takes in the key and returns the value from the table.    
contains: Takes in the key and returns a boolean, indicating if the key exisits in the table already.  