class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        candidates.sort()
        
        def backtrack(remaining, combo, start_index):
            if remaining == 0:
                result.append(list(combo))
                return
            
            for i in range(start_index, len(candidates)):
  
                if candidates[i] > remaining:
                    break
                
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                combo.append(candidates[i])
                # Move to i + 1 because each number can be used only once
                backtrack(remaining - candidates[i], combo, i + 1)
                combo.pop()
                
        backtrack(target, [], 0)
        return result