class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Loop through each cell
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                box = (r // 3, c // 3)
                # Check if cell is empty
                if cell == '.':
                    continue
                # Check if there's any duplicates in row, col, or box
                if (
                    cell in rows[r] or 
                    cell in cols[c] or 
                    cell in boxes[box]
                ): return False
                # Add cell to all 3 dicts
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box].add(cell)
        # No duplicates -> return True
        return True
