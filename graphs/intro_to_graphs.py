import random
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def preorder_traversal(cls, root: 'TreeNode') -> List[int]:
        visited = []
        def dfs(node: TreeNode):
            if not node: return

            visited.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return visited

    @classmethod
    def inorder_traversal(cls, root: 'TreeNode') -> List[int]:
        visited = []
        def dfs(node: TreeNode):
            if not node: return

            dfs(node.left)
            visited.append(node.val)
            dfs(node.right)

            return

        dfs(root)
        return visited

    @classmethod
    def postorder_traversal(cls, root: 'TreeNode') -> List[int]:
        visited = []
        def dfs(node: TreeNode):
            if not node: return

            dfs(node.left)
            dfs(node.right)
            visited.append(node.val)

            return

        dfs(root)
        return visited

    @classmethod
    def level_order_traversal(cls, root: 'TreeNode') -> List[int]:
        if not root:
            return []

        nodes_to_visit = deque([root])
        result = []

        while nodes_to_visit:
            level = []
            for _ in range(len(nodes_to_visit)):
                current_node = nodes_to_visit.popleft()
                level.append(current_node.val)

                if current_node.left: nodes_to_visit.append(current_node.left)
                if current_node.right: nodes_to_visit.append(current_node.right)

            result.append(level)

        return result


    # Helper method to insert a node into a BST
    def insert_bst(self, val: int):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert_bst(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert_bst(val)



# MAIN
num_nodes_bst = 7
random_values = random.sample(range(1, 31), num_nodes_bst) # Get unique numbers

if not random_values:
    root_bst = None
else:
    root_bst = TreeNode(val=random_values[0])
    for i in range(1, num_nodes_bst):
        root_bst.insert_bst(random_values[i])


print("Generated values (in order of insertion):", random_values)
print("Root of BST:", root_bst.val)
print("Preorder Traversal of BST:", TreeNode.preorder_traversal(root_bst))
print("Inorder Traversal of BST:", TreeNode.inorder_traversal(root_bst))
print("Inorder Traversal of BST:", TreeNode.level_order_traversal(root_bst))


