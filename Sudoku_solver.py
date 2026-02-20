class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if self.is_safe(board, r, c, num):
                            board[r][c] = num
                            
                            # If this guess leads to a solution, stop
                            if self.solve(board):
                                return True
                            
                            # Otherwise, backtrack
                            board[r][c] = "."
                            
                    return False  # Trigger backtracking if no numbers 1-9 work
        return True # Board is full

    def is_safe(self, board, r, c, num):
      
        for i in range(9):
            if board[r][i] == num or board[i][c] == num:
                return False
        
        # Check 3x3 sub-box
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
                    
        return True

        # first commit