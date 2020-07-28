# Python-Code-Test

## 1) Write the following function’s body. A nested dictionary is passed as parameter. You need to print all keys with their depth.

run  python problem-1.py

```
def print_depth(data, d=1):
    def find_depth(dictonary, depth):
        for key in dictonary.keys():
            print(key, depth)
            if type(dictonary[key]) is type({}):
                find_depth(dictonary[key], depth+1)        
    find_depth(data, d)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a)
```

## 2) Write a new function with same functionality from Question 1, but it should be able to handle a Python object in addition to a dictionary from Question 1.

run python problem-2.py

```
class Person(object):
    def __init__(self, first_name=None, last_name=None, father=None):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

def print_person(person, depth):
    print("first_name: ", depth)
    print("last_name: ", depth)
    print("father: ", depth)    
    if person.father:
      print_person(person.father, depth+1)
    
def print_depth(data, d=1):
    def find_depth(dictonary, depth):
        for key in dictonary.keys():
            print(key, depth)
            if isinstance(dictonary[key], dict):
                find_depth(dictonary[key], depth+1)
            if isinstance(dictonary[key], Person):
                print_person(dictonary[key], depth+1) 
  
    find_depth(data, d)

person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
"key1": 1,
"key2": {
        "key3": 1,
    "key4": {
        "key5": 4,
        "User": person_b
    }}}

print_depth(a)
```

## 3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least Common Ancestor and print its value.

run python problem-3.py

```
class TreeNode:
    def __init__(self, x, parent=None):
        self.val = x
        self.parent = parent

class Solution:
    def lowest_common_ancestor(self, node1, node2):
        while node1:
            temp = node2
            while temp:
                #print(node1.val, temp.val)
                if temp.val == node1.val:
                    return node1.val
                temp = temp.parent
            node1 = node1.parent

a = TreeNode(1)
b = TreeNode(2,a)
c = TreeNode(3,a)
d = TreeNode(4,b)
e = TreeNode(8,d)
f = TreeNode(9,d)
g  = TreeNode(5, b)
h  = TreeNode(6, c)
i = TreeNode(7,c)

a = Solution()

print(a.lowest_common_ancestor(c,i))

```

### Program Complexity
- TimeComplexity: O(h^2)
- SpaceComplexity O(1)
