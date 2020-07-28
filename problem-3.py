'''
3) Write following functions body. 2 Nodes are passed as parameter. You need to find Least
Common Ancestor and print its value.
'''

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

# TimeComplexity: O(h^2)
# SpaceComplexity O(1)