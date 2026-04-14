# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: #if root is empty or end up before the subtree ends
            return False
        if not subRoot: #if subtree end that means all values are matched
            return True
        if self.sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)) #move to lower branches and check for subtree patterns
        
        
        if root.val == subRoot.val:
            return (self.isSubtree(root.left,subRoot.left) and self.isSubtree(root.right,subRoot.right))
    def sameTree(self, root , subRoot):
        if not root and not subRoot : #check if nothing is coming means it's null
            return True
        if root and subRoot and root.val == subRoot.val: #if both the trees are not empty and values are same
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))
        return False