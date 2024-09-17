class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lmaxdepth = self.dfs(root.left, 0, 0)
        rmaxdepth = self.dfs(root.right, 0, 0)
        
        if abs(lmaxdepth - rmaxdepth) > 1 or lmaxdepth < 0 or rmaxdepth < 0:
            return False
        return True

    def dfs(self, root: Optional[TreeNode], maxdepth: int, depth: int) -> int:
        if root is None:
            if depth > maxdepth:
                maxdepth = depth
            return maxdepth
        depth_cpy = depth
        depth_cpy += 1
        lmaxdepth = self.dfs(root.left, maxdepth, depth_cpy)
        rmaxdepth = self.dfs(root.right, maxdepth, depth_cpy)
        if abs(lmaxdepth-rmaxdepth) > 1:
            return -1
        return max(lmaxdepth, rmaxdepth)
        
