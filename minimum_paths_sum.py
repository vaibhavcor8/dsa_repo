class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
    
        dp = [float('inf')] * n
        
        dp[0] = 0
        
        for r in range(m):
            for c in range(n):
                if c == 0:
                   
                    dp[c] += grid[r][c]
                else:
                
                    dp[c] = grid[r][c] + min(dp[c], dp[c-1])
                    
        return dp[-1]