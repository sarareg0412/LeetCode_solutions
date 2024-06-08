# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = self.level(root,{},0)
        result = []
        if hashmap != None:
            for key in list(hashmap.keys()):
                result.append(hashmap[key])
        
        return result


    def level(self, root, hashmap, lev):
        if root == None:
            return
        
        if lev in hashmap:
            hashmap[lev].append(root.val)
        else:
            hashmap[lev] = [root.val]
        
        self.level(root.left,hashmap,lev+1)
        self.level( root.right,hashmap,lev+1)

        return hashmap