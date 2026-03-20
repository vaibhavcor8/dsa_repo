import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        numbers = [str(i) for i in range(1, n + 1)]
        
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i-1] * i
            

        k -= 1
        res = []
        
        for i in range(n - 1, -1, -1):
          
            idx = k // factorials[i]
            k %= factorials[i]
            
            res.append(numbers.pop(idx))
            
        return "".join(res)


        # first commit