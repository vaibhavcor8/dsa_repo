class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Result can have at most m + n digits
        res = [0] * (m + n)
        
        # Multiply digits from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Calculate product of current digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add product to the current sum at p2
                total = mul + res[p2]
                
                # Update positions
                res[p2] = total % 10
                res[p1] += total // 10
        
        # Convert list to string, skipping leading zero if it exists
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        return "".join(map(str, res[start:]))

        # first commit