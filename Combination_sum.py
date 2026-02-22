class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining, combo, start_index):
         
            if remaining == 0:
                result.append(list(combo))
                return
        
            if remaining < 0:
                return
            
            for i in range(start_index, len(candidates)):
          
                combo.append(candidates[i])
                
                backtrack(remaining - candidates[i], combo, i)
                
                combo.pop()
                
        backtrack(target, [], 0)
        return result
    
    # first commit