class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize list of sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Ignore empty cells
                if val == ".":
                    continue
                
                # Determine which 3x3 box the cell belongs to
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if the value already exists in the current row, column, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Add value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True