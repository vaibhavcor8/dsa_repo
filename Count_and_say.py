class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Start with the base case
        current_str = "1"
        
        # We need to perform the transformation n-1 times
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            # Run-length encoding logic
            while i < len(current_str):
                count = 1
                # While the next character is the same as the current one
                while i + 1 < len(current_str) and current_str[i] == current_str[i+1]:
                    i += 1
                    count += 1
                
                # Append [count][digit]
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            
            # Join list to form the new string
            current_str = "".join(next_str)
            
        return current_str