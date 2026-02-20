class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Step 1: Pre-populate our sets and find all empty spots
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index):
            if index == len(empty_cells):
                return True  # All cells filled!

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo (Backtrack)
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
                    board[r][c] = "."
            
            return False

        backtrack(0)

        # first commit