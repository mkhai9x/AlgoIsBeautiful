'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
            1
           / \
          2   3
         / \
        4   5   
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def helper(root, diameter):
    if root == None:
        return 0
    left = helper(root.left, diameter)
    right = helper(root.right, diameter)
    diameter[0] = max(diameter[0], left + right + 1)
    return max(left, right) + 1


def diameterOfBinaryTree(root):
    diameter = [-1]
    helper(root, diameter)
    return diameter[0] - 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    assert diameterOfBinaryTree(root) == 3

    root = Node(1)

    assert diameterOfBinaryTree(root) == 0
